import sys

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

current_schem = [-1,-1,-1,-1,-1, None]

keys = []
locks = []

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line or linecontent == "":
        if current_schem[5] == "key":
            keys.append(current_schem[:-1])
        else:
            locks.append(current_schem[:-1])
        current_schem = [-1,-1,-1,-1,-1, None]
        if not line:
            break
        continue
    
    if current_schem[5] is None and linecontent[0] == ".":
        current_schem[5] = "key"
    elif current_schem[5] is None:
        current_schem[5] = "lock"
    for i in range(len(linecontent)):
        if linecontent[i] == "#":
            current_schem[i]+=1

pairs = 0
for lock in locks:
    for key in keys:
        overlap = False
        for i in range(len(key)):
            if key[i] + lock[i] > 5:
                overlap = True
        if not overlap:
            pairs+=1

print("Part 1:", pairs)
