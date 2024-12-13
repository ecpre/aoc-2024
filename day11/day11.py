import sys
from collections import Counter

if len(sys.argv) < 2:
    print("must have an argument")
    exit

ifile = open(sys.argv[1], 'r')

count = int(sys.argv[2])

line = ifile.readline()
linecontent = line.strip()

stones = linecontent.split(' ')

stonedict = dict(Counter(stones))
print(stonedict)

i = 0

stonemap = {}

print(stones)
while i < count:
    newstonedict = stonedict.copy()
    for stone, freq in stonedict.items():
        if freq == 0:
            continue
        if stone == "0":
            if "1" not in newstonedict:
                newstonedict["1"]=0
            newstonedict["1"]+=freq
        elif len(stone) %2 == 0:
            leftstone = stone[0:len(stone)//2]
            rightstone = str(int(stone[len(stone)//2:]))
            if leftstone not in newstonedict:
                newstonedict[leftstone] = 0
            if rightstone not in newstonedict:
                newstonedict[rightstone] = 0
            newstonedict[leftstone]+=freq
            newstonedict[rightstone]+=freq
        else:
            newstone = str(int(stone)*2024)
            if newstone not in newstonedict:
                newstonedict[newstone]=0
            newstonedict[newstone]+=freq
        newstonedict[stone]-=freq
    stonedict = {key: value for key, value in newstonedict.items() if value!=0}
    i+=1

filtered = {key: value for key, value in stonedict.items() if value!= 0}
print(str(sum(filtered.values())))
