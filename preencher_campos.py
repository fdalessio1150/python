import re

data = open("C:\\Users\\Felipe\\Desktop\\dados.txt", encoding="utf8", mode="r+")
format = open("C:\\Users\\Felipe\\Desktop\\formato.txt", encoding="utf8", mode="r+")
newFile = open("C:\\Users\\Felipe\\Desktop\\result.txt", encoding="utf8", mode="w+")
columns = data.readline().replace(' ', '').replace("\n", "").split(',')

dataSize = len(data.readlines())
formatSize = len(format.readlines())
columnsSize = len(columns)
delimiter = ',\n'

combs = []
a = []

data.seek(0)
format.seek(0)

for x in range(dataSize):
    format.seek(0)
    for count, line in enumerate(format):
        if count == (formatSize-1) and dataSize > 1 and x != dataSize - 1:
             a.append(line + delimiter)
        elif count == 0 or count == formatSize-1:
            a.append(line)
        elif x == (dataSize-1) and count == (formatSize-1) and dataSize > 1:
            a.append(line)           
        else:
            a.append(str(line))
print("Primeiro loop - OK")

for dataLine in data.readlines()[1:]:
    data = dataLine.replace(', ',',').replace('\n', '').split(',')
    for x in range(len(columns)):
        combs.append((columns[x], data[x]))
print("Segundo loop - OK")

for k, v in combs:
    for i,line in enumerate(a):
        if re.search(k, line):
            a[i] = line.replace(k, v)
            break            
print("Terceiro loop - OK")

for v in a:
    print(v)
    newFile.write(v)
