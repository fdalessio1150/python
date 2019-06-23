import re
import sys
import os
from string import Template

path = "C:\\Users\Felipe\\Desktop\\"
dataFileName = "dados.txt"
formatFileName = "formato.txt"
newFileName = "result.txt"
dataFileDelimiter = ','

def main():
    formatFile = readFormatFile()
    (lines, header) = readDataFile()
    newFile = createNewFile()
    
    combine(lines, header, formatFile, newFile)

def createNewFile():
    if os.path.exists(path):
        return open(path + newFileName, encoding="utf-8", mode="w+")
    else:
        print("ERROR - directory doesn't exists.")  

def readDataFile():
    if os.path.exists(path):
        try:
            dataFile = open(path + dataFileName, encoding="utf-8", mode="r")
            formatFile = open(path + formatFileName, encoding="utf-8", mode="r")
            
            lines = [line.strip() for line in dataFile.readlines()]
            header = lines[0]
            lines = lines[1:]
            
            return lines, header
        except IOError:
            print("ERROR - data file may not exists.")            
    else:
        print("ERROR - directory doesn't exists.")

def readFormatFile():
    if os.path.exists(path):
        try:
            formatFile = open(path + formatFileName, encoding="utf-8", mode="r")
            return Template(formatFile.read())
        except IOError:
            print("ERROR - format file may not exists.") 

def combine(lines, header, formatFile, newFile):
    header = header.strip().split(dataFileDelimiter)
    
    for line in lines:
        data = line.split(',')
        combs = []
        for x in range(len(header)):
            combs.append((header[x], data[x]))
            if x == (len(header) - 1):
                subDictionary = {k:v for k, v in combs}
                writeFile(formatFile, subDictionary, newFile)

def writeFile(formatFile, subDictionary, newFile):
    newFile.write(formatFile.substitute(subDictionary))

if __name__ == "__main__":
    main()
