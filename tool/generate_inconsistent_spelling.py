# --------------------------------------------------
# import
# --------------------------------------------------
import pyperclip
from itertools import product

from typing import Optional


# --------------------------------------------------
# global
# --------------------------------------------------
WORD_SEPARATORS = ["", " ", "-", "_"]


# --------------------------------------------------
# func
# --------------------------------------------------
def generate():
    org = pyperclip.paste()
    orgs = org.splitlines()

    ans = []
    for org in orgs:
        inner_ans = []
        org_elements = org.split("_")
        for seps in product(WORD_SEPARATORS, repeat=len(org_elements) - 1):
            # 区切り文字リストのサイズを、検索キーワード単語リストのサイズに一致させる
            seps = list(seps)
            seps.extend(["" for _ in range(len(org_elements) - len(seps))])

            # 検索キーワード単語リストを、区切り文字リストで連結する
            temp = "".join(c + s for c, s in zip(org_elements, seps))
            inner_ans.append(temp)

        ans.extend(inner_ans)

    pyperclip.copy("\n".join(ans))


# --------------------------------------------------
# main
# --------------------------------------------------
if __name__ == "__main__":
    generate()
