import sys
from functools import cache

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

line = ifile.readline()
linecontent = line.strip()

towels = linecontent.split(", ")

designs = []
totalmeans = 0

@cache
def validate_design(current, design):
    curlen = len(current)
    meanscount = 0
    for towel in towels:
        if current + towel == design[:len(current)+len(towel)]:
            if current+towel == design:
                meanscount+=1
                continue
            ret = validate_design(current+towel, design)
            meanscount+=ret
    return meanscount

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    if linecontent == "":
        continue
    
    validated = validate_design("", linecontent)
    if validated:
        designs.append(linecontent)
    totalmeans += validated
    
print("Part 1: " + str(len(designs)))
print("Part 2: " + str(totalmeans))

