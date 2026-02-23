# --------------------------------------------------
# import
# --------------------------------------------------
from itertools import product
import json
import re
from pprint import pprint

from typing import Optional

from logger import LOGGER
from define import FULLPATH_INTERMEDIATE_JSON, SEARCH_MODE_TYPE, SEARCH_MODE_LIST
from basic_func import get_setting, get_file_path_recurcive_as_list
from data_structure_cell import CellData


# --------------------------------------------------
# class
# --------------------------------------------------
class PowerSearch:
    def __init__(self, search_mode: SEARCH_MODE_TYPE, snake_case_search_pattern: str) -> None:
        LOGGER.info(f"開始します")
        LOGGER.info(f"JSONファイル格納ディレクトリ: {FULLPATH_INTERMEDIATE_JSON}")

        assert search_mode in SEARCH_MODE_LIST
        self.search_mode: SEARCH_MODE_TYPE = search_mode
        self.snake_case_search_pattern = snake_case_search_pattern

        LOGGER.info(f"検索モード: {search_mode}")
        LOGGER.info(f"検索キーワード: {snake_case_search_pattern}")

    # ------------------------------
    # main
    # ------------------------------

    def search(self) -> list[CellData]:
        results: list[CellData] = []

        # ----------
        # 前準備
        # ----------
        match self.search_mode:
            case "text":
                # 検索キーワードの表記ゆれキーワードを生成する
                search_pattern_list = self.generate_search_pattern_list(self.snake_case_search_pattern)

            case _ if self.search_mode in ["text_color", "fill_color", "is_strike"]:
                LOGGER.warning("未サポートです。終了します")
                exit(1)

        # ----------
        # 検索処理
        # ----------
        LOGGER.info(f"検索開始")

        # 全てのJSONファイルを検索する
        json_path_list = get_file_path_recurcive_as_list(FULLPATH_INTERMEDIATE_JSON, [".json"])
        for json_path in json_path_list:
            # JSONファイルをCellDataとして読み込む
            cell_data_list = self.convert_json_to_cell_data_list(json_path)

            # search_modeで分岐する
            match self.search_mode:
                # テキスト検索
                case "text":
                    # 表記ゆれキーワードを使って、CellDataの中から検索キーワードに引っかかったCellDataを取得する
                    result = self.search_text(cell_data_list, search_pattern_list)
                    if result:
                        results.extend(result)
                case _ if self.search_mode in ["text_color", "fill_color", "is_strike"]:
                    LOGGER.warning("未サポートです。終了します")
                    exit(1)

        LOGGER.info(f"検索完了")

        return results

    # ------------------------------
    # common
    # ------------------------------
    def generate_search_pattern_list(self, snake_case_search_pattern: str) -> list[str]:
        ans = []

        # _で区切った検索キーワードの単語リスト
        search_pattern_elements = snake_case_search_pattern.split("_")

        # 区切り文字リストのデカルト積で検索キーワード派生リストを生成する
        word_separators = get_setting(["word_separators"])
        for seps in product(word_separators, repeat=len(search_pattern_elements) - 1):
            # 区切り文字リストのサイズを、検索キーワード単語リストのサイズに一致させる
            seps = list(seps)
            seps.extend(["" for _ in range(len(search_pattern_elements) - len(seps))])

            # 検索キーワード単語リストを、区切り文字リストで連結する
            temp = "".join(c + s for c, s in zip(search_pattern_elements, seps))
            ans.append(temp)

        return ans

    # ------------------------------
    # common
    # ------------------------------
    def convert_json_to_cell_data_list(self, json_path: str) -> list[CellData]:
        # 形式: [CellData, CellData, ..., CellData]
        cell_data_list: list[CellData] = []

        # JSONファイルを読む
        with open(json_path, "r", encoding="utf-8") as f:
            # 形式: [{セルデータ辞書}, {セルデータ辞書}, ..., {セルデータ辞書}]
            json_data_list: list[dict] = json.load(f)

            # 全てのセルデータ辞書を舐める
            for cell_data in json_data_list:
                temp = CellData.from_dict(cell_data)  # セルデータ辞書をCellDataに変換
                cell_data_list.append(temp)

        return cell_data_list

    # ------------------------------
    # search_mode = text
    # ------------------------------
    def search_text(self, cell_data_list: list[CellData], search_pattern_list: list[str]) -> Optional[list[CellData]]:
        results: list[CellData] = []

        # 表記ゆれキーワードを使って検索する
        for search_pattern in search_pattern_list:
            result = self.search_text_search_pattern(cell_data_list, search_pattern)
            if result is not None:
                results.extend(result)

        # 空ではないresultのみreturnする
        if len(results):
            return results
        else:
            return None

    # ------------------------------
    # search_mode = text
    # ------------------------------
    def search_text_search_pattern(self, cell_data_list: list[CellData], search_pattern: str) -> Optional[list[CellData]]:
        result: list[CellData] = []

        # 検索キーワード
        regex: re.Pattern = re.compile(search_pattern)

        # 全てのCellDataを舐める
        for cell_data in cell_data_list:
            # CellData.dataが検索キーワードに引っかかったら、resultに追加
            if regex.search(cell_data.text):
                result.append(cell_data)

        # 空ではないresultのみreturnする
        if len(result):
            return result
        else:
            return None


# --------------------------------------------------
# main
# --------------------------------------------------
if __name__ == "__main__":
    search_mode = get_setting(["search", "mode"])
    search_word = get_setting(["search", "snake_case_word"])
    cell_data_list = PowerSearch(search_mode, search_word).search()

    for cell_data in cell_data_list:
        pprint(cell_data.to_dict())
