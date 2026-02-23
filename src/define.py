# --------------------------------------------------
# import
# --------------------------------------------------
from typing import Literal
from basic_func import get_setting


# --------------------------------------------------
# global
# --------------------------------------------------
SETTING_FILE = "setting.yaml"

FULLPATH_ORIGINAL_EXCEL = get_setting(["full_path", "original_excel"])
FULLPATH_INTERMEDIATE_JSON = get_setting(["full_path", "intermediate_json"])

EXCEL_EXTENSIONS = get_setting(["excel_extensions"])

COLOR_DEFAULT = "default_color"

SEARCH_MODE_TYPE = Literal["text", "text_color", "fill_color", "is_strike"]
SEARCH_MODE_LIST = ["text", "text_color", "fill_color", "is_strike"]
