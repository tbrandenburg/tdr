import os
import sys
import argparse
import pprint
import json
import sys

from datetime import date

def tdr_template(title):
    tpl = {
        "brief": title,
        "author": os.getlogin(),
        "date": date.today().strftime("%Y-%m-%d"),
        "description": "",
        "category": "techdebt",
        "severity": "warning",
        "priority": "",
        "file": ".",
        "line": 0,
        "column": 0,
        "votes": 1,
        "discussion": []
    }
    return tpl


def tdr_new(dir, title):
    if type(title) == list:
        title_dashed = "-".join(title).replace(' ', '-')
        title_spaced = " ".join(title)
    elif type(title) == str:
        title_dashed = (title).replace(' ', '-')
        title_spaced = title

    tdrFilePath = os.path.join(os.path.abspath(
        dir), ".tdr", title_dashed+".tdr")

    # Create directories
    os.makedirs(os.path.dirname(tdrFilePath), exist_ok=True)

    # Create TDR file if not exist
    if not os.path.exists(tdrFilePath):
        with open(os.path.abspath(tdrFilePath), "w") as jsonFile:
            tpl = tdr_template(title_spaced)
            jsonObj = json.dumps(tpl, indent=4)
            jsonFile.write(jsonObj)
            print("[TDR] Created TDR: " + tdrFilePath)
    else:
        print("[TDR] TDR already present: " + tdrFilePath)


def main():
    parser = argparse.ArgumentParser(
        prog='tdr_new',
        description='Technical Debt Record Tool - Create new technical debt')
    parser.add_argument('title', metavar='Title of TDR',
                        nargs='+', help='Title of the TDR')
    parser.add_argument("--path", "-p", help="Path", type=str, default=".")

    args = parser.parse_args()

    tdr_new(args.path, args.title)

    return 0


if __name__ == '__main__':
    sys.exit(main())
