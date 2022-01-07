# -*- coding: utf-8 -*-
import argparse
from os import path
import json

parser = argparse.ArgumentParser()

parser.add_argument("--config","-c", help="File format .json with settings")
parser.add_argument("--file","-f", help="File to edit")
args = parser.parse_args()

if args.config and args.file:
    try:
        with open(args.config, "r") as file_config:
            settings = json.load(file_config)

    except FileNotFoundError:
        print("Config not found")
else:
    print("Write --help for help")
    exit()

file_name = path.abspath(args.file)

try:
    with open(file_name, "rb+") as file:
        data = file.read()
        hex_old = bytes.fromhex(settings["hex_old"])
        offset = data.find(hex_old)+settings["offset"]

        for i in range(data.count(hex_old)):
            if offset != -1:
                file.seek(offset)
                hex_new = bytes.fromhex(settings["hex_new"])
                file.write(hex_new)
                print("Rewrite")

            else:
                print("Bytes not found")

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Please, close the file")
