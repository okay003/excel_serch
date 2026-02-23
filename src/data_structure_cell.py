# --------------------------------------------------
# import
# --------------------------------------------------
from openpyxl.cell.cell import Cell

from define import COLOR_DEFAULT


# --------------------------------------------------
# global
# --------------------------------------------------
COLOR_DEFAULT_FILL_COLOR = "00000000"


# --------------------------------------------------
# class
# --------------------------------------------------
class CellData:
    def __init__(self, cell: Cell) -> None:
        # 座標
        self.cordinate: str = cell.coordinate

        # データ
        self.data: str = str(cell.value)

        # テキスト色
        self.format_text_color: str = COLOR_DEFAULT
        if "rgb" in cell.font.color.__dict__:
            self.format_text_color = cell.font.color.rgb

        # 塗りつぶし色
        self.format_fill_color: str = COLOR_DEFAULT
        if cell.fill.fgColor.rgb != COLOR_DEFAULT_FILL_COLOR:
            self.format_fill_color = cell.fill.fgColor.rgb

        # 打消し線の有無
        self.format_is_strike: bool = True if cell.font.strike is not None else False

    def to_dict(self) -> dict[str, str | bool]:
        return self.__dict__
