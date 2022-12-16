import requests
from key import cookie

def get_data(day, split_lines=True):
    input_location = f"https://adventofcode.com/2022/day/{day}/input"
    headers = {
        "cookie": cookie
    }
    r = requests.get(input_location, headers=headers)
    if split_lines:
        return r.text.rstrip().split(u"\n")
    else:
        return r.text.rstrip()