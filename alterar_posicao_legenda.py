import re
from datetime import timedelta

newf = open("C:/Users/Felipe/Desktop/legenda_final.srt", encoding="utf8", mode="w+")

with open("C:/Users/Felipe/Desktop/legenda.srt", encoding="utf8", mode="r+") as f:
    pattern = r"\d\d:\d\d:\d\d,\d\d\d"
    for i,line in enumerate(f):
        if re.match(pattern, line):
            timestamps = line.replace(" --> ", " ").replace("\n", "").split(" ")
            
            firsttime = timestamps[0].split(":")
        
            firsthour = firsttime[0]
            firstminute = firsttime[1]
            firsttimes = firsttime[2].split(",")
            firstsecond = firsttimes[0]
            firstmillisecond = firsttimes[1]
            
            first = timedelta(hours=int(firsthour), minutes=int(firstminute), seconds=int(firstsecond), milliseconds=int(firstmillisecond))
            
            secondtime = timestamps[1].split(":")
                
            secondhour = secondtime[0]
            secondminute = secondtime[1]
            secondtimes = secondtime[2].split(",")
            secondsecond = secondtimes[0]
            secondmillisecond = secondtimes[1]
            
            second = timedelta(hours=int(secondhour), minutes=int(secondminute), seconds=int(secondsecond), milliseconds=int(secondmillisecond))
                        
            newf.write(str(first + timedelta(seconds=8)).replace(".",",")[0:11].zfill(12) + " --> " + str(second + timedelta(seconds=7)).replace(".",",")[0:11].zfill(12) + "\n")
        else:
            newf.write(line)
