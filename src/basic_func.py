# --------------------------------------------------
# import
# --------------------------------------------------
import os
from pathlib import Path

from typing import Any


# --------------------------------------------------
# func
# --------------------------------------------------
def get_setting(keys: list[str]) -> Any:
    """
    setting.yamlから、指定されたキーで値を取得する関数。
    """
    import yaml
    from define import SETTING_FILE

    with open(SETTING_FILE, "r") as f:
        setting = yaml.safe_load(f)

        for k in keys:
            setting = setting[k]

        return setting


def create_dir(full_path: str) -> None:
    from logger import LOGGER

    if not os.path.exists(full_path):
        os.mkdir(full_path)
        LOGGER.info(f"ディレクトリを生成しました: {full_path}")


def get_file_path_recurcive_as_list(path: str, extension_list_with_dot: list[str]) -> list[str]:
    """
    指定されたパスを再帰的に探索し、指定された拡張子のファイルの絶対パスをリストにして返す関数。
    """
    from logger import LOGGER

    root = Path(path)

    ans = []
    for ext in extension_list_with_dot:
        temp = [str(p.resolve()) for p in root.rglob(f"*{ext}")]
        ans.extend(temp)
        LOGGER.debug(f"検出しました: {len(temp)}")

    LOGGER.info(f"検出しました: {len(ans)}")

    return ans
