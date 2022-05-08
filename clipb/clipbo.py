import sys
from venv import create
import pyperclip
import json

SAVED_DATA = "clipboard.json"

#create a json file for us and one to read one
def save_data(filepath, data):
    #Opens a file, sets in write mode
    with open(filepath, "w") as f:
        json.dump(data, f)
        #json.dump dumps data to file path (f).

#save_data("test.json", {"key": "value"})
#create a json file to read
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = pyperclip.paste()
        #save_data(filepath, data)
        save_data(SAVED_DATA, data)
        print('Data saved!')
    elif command == "load":
        #ask user for key and then verify key exists if not errpr
        key = input("Enter a key: ")
        if key in data:
            pyperclip.copy(data[key])
            print("Data copied to clipboard.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command")

#Happy Mothers Day