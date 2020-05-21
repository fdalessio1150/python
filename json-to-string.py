import os
import json

path = "/home/felipe/applications/python/data-generators/"
new_file_name = "json-string-v2.txt"

file_name = "data-v2.json"
json_group = "data"

def create_new_file():
    if os.path.exists(path):
        return open(path + new_file_name, encoding="utf-8", mode="w+")
    else:
        print("ERROR - directory doesn't exists.") 

def read_json_file():
    if os.path.exists(path):
        try:
            json_file = open(path + file_name, encoding="utf-8", mode="r")

            return json.load(json_file)
        except IOError:
            print("ERROR - data file may not exists.")            
    else:
        print("ERROR - directory doesn't exists.")

def main():
    data = read_json_file()
    new_file = create_new_file()

    for i in data[json_group]: 
            new_file.write(str(i) + "\n")

if __name__ == "__main__":
    main()