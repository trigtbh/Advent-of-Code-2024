import requests

import os
basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.join(basepath, "cookie.txt")) as f:

    cookies = {"session": f.read()}

def get_input(year, day):
    if not os.path.exists(os.path.join(basepath, "inputs", f"{day}.txt")):
        contents = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies).text
        with open(os.path.join(basepath, "inputs", f"{day}.txt"), "w") as f:
            f.write(contents.strip())
    else:
        with open(os.path.join(basepath, "inputs", f"{day}.txt"), "r") as f:
            contents = f.read().strip()
    return contents
