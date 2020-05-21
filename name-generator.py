import os
from faker import Faker
fake = Faker(['pt_BR'])

path = "/home/felipe/applications/python/data-generators/"
new_file_name = "name-generator.txt"

def create_new_file():
    if os.path.exists(path):
        return open(path + new_file_name, encoding="utf-8", mode="w+")
    else:
        print("ERROR - directory doesn't exists.")  

def main():
    new_file = create_new_file()
    for i in range(20000):
        new_file.write(fake.name() + "\n")
	
if __name__ == "__main__":
    main()