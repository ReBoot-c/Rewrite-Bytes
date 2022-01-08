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
        exit(0)
    except PermissionError:
        print("Permission error")
        exit(0)
    except Exception as ex:
        print("Unknow error: \n {}".format(ex))
        exit(0)
else:
    print("Write --help for help")
    exit()

file_name = path.abspath(args.file)

try:
    with open(file_name, "rb+") as file:
        data = file.read()
        hex_old = bytes.fromhex(settings["hex_old"])
        offset = data.find(hex_old)

        for i in range(data.count(hex_old)):
            if offset != -1:
                file.seek(offset)
                hex_new = bytes.fromhex(settings["hex_new"])
                file.write(hex_new)
                

            else:
                print("Bytes not found")
                exit(0)
        print("Rewrite")

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission error")
except Exception as ex:
    print("Unknow error: \n {}".format(ex))
