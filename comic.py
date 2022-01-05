#!/usr/bin/python
import requests
import random
import argparse
import sys

class UIColors:
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    RESET = '\033[0;0m'


def display_ui(chosen_comic, license_attrib):
    sys.stdout.write("\n" + UIColors.BOLD + chosen_comic["safe_title"] + "\n")
    sys.stdout.write(UIColors.RESET)
    sys.stdout.write(UIColors.GREEN + chosen_comic["transcript"].strip() + "\n")
    sys.stdout.write("\n" + UIColors.BOLD + "©" + chosen_comic["year"] + license_attrib + "\n\n")
    sys.stdout.write(UIColors.RESET)


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--Number", help="Choose a comic number")
args = parser.parse_args()
copyright_holder = ' Randall Munroe - xkcd.com Licensed under CC BY-NC 2.5'

current = requests.get("https://xkcd.com/614/info.0.json").json()
current_number = current["num"]
random_comic_number = random.randint(1, current_number)
if args.Number:
    choice = current = requests.get("https://xkcd.com/" + str(args.Number) + "/info.0.json").json()
    display_ui(choice,copyright_holder)
else:
    display_ui(current, copyright_holder)
