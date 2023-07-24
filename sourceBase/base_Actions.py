import subprocess
from find_Text import FindText


class BaseAction:

    @staticmethod
    def click(text, partial=False):
        try:
            x, y = FindText.get_text(text, partial)
            subprocess.run(["adb", "-s", "104e6ae3", "shell", "input", "tap", str(x), str(y)], check=True,
                           shell=True)
        except subprocess.CompletedProcess as e:
            raise e

    @staticmethod
    def isPresent(text, partial=False):
        try:
            dump_result = FindText.get_text(text, partial)
            if dump_result is not None:
                print(f"'{text}' is present")
        except Exception as e:
            raise e
