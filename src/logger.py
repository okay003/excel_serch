# --------------------------------------------------
# import
# --------------------------------------------------
import sys
import logging


# --------------------------------------------------
# func
# --------------------------------------------------
def generate_logger(name: str) -> logging.Logger:
    """
    Loggerを生成する関数。
    """
    from rainbow_logging_handler import RainbowLoggingHandler
    from basic_func import get_setting

    formatter = logging.Formatter(" | ".join(["%(levelname)s", "%(message)s", "%(filename)s", "%(funcName)s"]))

    # ------------------------------
    # root設定
    # ------------------------------
    root = logging.getLogger(name)
    root.setLevel(logging._nameToLevel[get_setting(["log_level"])])

    # ------------------------------
    # ターミナル用
    # ------------------------------
    terminal_handler = RainbowLoggingHandler(sys.stderr)
    terminal_handler.setFormatter(formatter)
    root.addHandler(terminal_handler)

    return root


# --------------------------------------------------
# global
# --------------------------------------------------
LOGGER = generate_logger(__name__)
