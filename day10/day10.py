import sys

if len(sys.argv) < 2:
    print("must have argument")
    exit

ifile = open(sys.argv[1], 'r')

topomap = []
scores = []
totalscore = 0
trailscores = 0

def get_adjacent(i, j):
    current = topomap[i][j]
    adjacent = []
    if i > 0 and topomap[i-1][j]-current == 1:
        adjacent.append((i-1, j))
    if j > 0 and topomap[i][j-1]-current == 1:
        adjacent.append((i, j-1))
    if i < len(topomap)-1 and topomap[i+1][j]-current == 1:
        adjacent.append((i+1, j))
    if j < len(topomap[i])-1 and topomap[i][j+1]-current == 1:
        adjacent.append((i, j+1))
    return adjacent

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break
    
    maprow = []
    for i in range(len(linecontent)):
        maprow.append(int(linecontent[i]))
    
    topomap.append(maprow)

nines = set()

def find_paths(i, j):
    if topomap[i][j] == 9:
        nines.add((i,j))
        return 1
    adj = get_adjacent(i,j)
    if not adj:
        return 0
    retval = 0
    for a in adj:
        retval+= find_paths(a[0],a[1])
    return retval

for i in range(len(topomap)):
    for j in range(len(topomap[i])):
        if topomap[i][j] != 0:
            continue
        trailscore = find_paths(i,j)
        trailscores+=trailscore
        totalscore+=len(nines)
        nines.clear()

print(totalscore)
print(trailscores)


