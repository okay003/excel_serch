# --------------------------------------------------
# import
# --------------------------------------------------
from openpyxl.cell.cell import Cell

from typing import Optional

from define import COLOR_DEFAULT


# --------------------------------------------------
# global
# --------------------------------------------------
COLOR_DEFAULT_FILL_COLOR = "00000000"


# --------------------------------------------------
# class
# --------------------------------------------------
class CellData:
    def __init__(self, book: Optional[str], sheet: Optional[str], cell: Optional[Cell]) -> None:
        # ファイル名
        self.book: str = book if book else ""

        # シート名
        self.sheet: str = sheet if sheet else ""

        # 座標
        self.cordinate: str = cell.coordinate if cell else ""

        # データ
        self.text: str = str(cell.value) if cell else ""

        # テキスト色
        self.format_text_color: str = COLOR_DEFAULT
        if cell and "rgb" in cell.font.color.__dict__:
            self.format_text_color = cell.font.color.rgb

        # 塗りつぶし色
        self.format_fill_color: str = COLOR_DEFAULT
        if cell and cell.fill.fgColor.rgb != COLOR_DEFAULT_FILL_COLOR:
            self.format_fill_color = cell.fill.fgColor.rgb

        # 打消し線の有無
        self.format_is_strike: bool = True if cell and cell.font.strike is not None else False

    def to_dict(self) -> dict[str, str | bool]:
        return self.__dict__

    @staticmethod
    def from_dict(cell_data_dict: dict):
        cell_data = CellData(None, None, None)
        cell_data.__dict__.update(cell_data_dict)
        return cell_data
