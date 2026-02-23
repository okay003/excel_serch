# --------------------------------------------------
# import
# --------------------------------------------------
from basic_func import get_setting


# --------------------------------------------------
# global
# --------------------------------------------------
SETTING_FILE = "setting.yaml"

FULLPATH_ORIGINAL_EXCEL = get_setting(["full_path", "original_excel"])
FULLPATH_INTERMEDIATE_JSON = get_setting(["full_path", "intermediate_json"])

EXCEL_EXTENSIONS = get_setting(["excel_extensions"])

COLOR_DEFAULT = "default_color"
