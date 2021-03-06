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
        print("Permission Error")
        exit(0)
    except Exception as ex:
        print("Unknow error: \n {}".format(ex))
        exit(0)
else:
    print("Write --help for help")
    exit()

file_name = path.abspath(args.file)


try:
    with open(file_name, "rb") as file:
        data = file.read()
    hex_old = [bytes.fromhex(i) for i in settings["hex_old"]]
    hex_new = [bytes.fromhex(i) for i in settings["hex_new"]]
    count = 0
    for i in hex_old:
        if i in data:
            count += 1 

    if count > 0:
        with open(file_name, "wb") as file_edit:
            for byte_replace in zip(hex_old, hex_new):
                data = data.replace(*byte_replace)
            file_edit.write(data)
            print("Rewrite: {}".format(count))
    else:
        print("Bytes not found")

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission error")
except Exception as ex:
    print("Unknow error: \n {}".format(ex))

