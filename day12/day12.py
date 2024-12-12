import sys

ifile = open(sys.argv[1], 'r')

visited = set()
edges = set()

regiondict = {}
areadict = {}

regionmap = []

def get_adjacent(i,j):
    current = regionmap[i][j]
    adjacent = []
    notadjacent = []
    adjacent_corners = []
    if i > 0 and regionmap[i-1][j] == current:
        adjacent.append((i-1, j))
    else:
        notadjacent.append((i-1,j))
    if j > 0 and regionmap[i][j-1] == current:
        adjacent.append((i, j-1))
    else:
        notadjacent.append((i,j-1))
    if i < len(regionmap)-1 and regionmap[i+1][j] == current:
        adjacent.append((i+1, j))
    else:
        notadjacent.append((i+1, j))
    if j < len(regionmap[i])-1 and regionmap[i][j+1] == current:
        adjacent.append((i, j+1))
    else:
        notadjacent.append((i,j+1))
    if i > 0 and j > 0 and regionmap[i-1][j-1] == current:
        adjacent_corners.append((i-1,j-1))
    if i > 0 and j < len(regionmap[i])-1 and regionmap[i-1][j+1] == current:
        adjacent_corners.append((i-1,j+1))
    if i < len(regionmap)-1 and j > 0 and regionmap[i+1][j-1] == current:
        adjacent_corners.append((i+1,j-1))
    if i < len(regionmap)-1 and j < len(regionmap[i])-1 and regionmap[i+1][j+1] == current:
        adjacent_corners.append((i+1,j+1))
    return [adjacent, notadjacent, adjacent_corners]

def get_measurements(i,j,region):
    retval = [0,0]
    adj = get_adjacent(i,j)
    retval[0] += len(adj[1])
    retval[1]+=1
    visited.add((i,j))
    regiondict[region].add((i,j))
    for a in adj[0]:
        if (a[0],a[1]) not in visited:
            neighbor_values = get_measurements(a[0],a[1],region)
            retval[0] += neighbor_values[0]
            retval[1] += neighbor_values[1]
    return retval

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    regionmap.append(linecontent)

totalprice = 0
for i in range(len(regionmap)):
    for j in range(len(regionmap[i])):
        if (i,j) in visited:
            continue
        regiondict[(i,j)] = set()
        area = 0
        perimeter = 0
        sides=[]
        measurements = get_measurements(i,j,(i,j))
        perimeter = measurements[0]
        area = measurements[1]
        areadict[(i,j)] = area
        totalprice += area*perimeter

totalprice2 = 0

edges_visited = set()

def is_corner(i,j):
    corners = 0
    edges_visited.add((i,j))
    adj = get_adjacent(i,j)
    ne = (i+1,j+1)
    nw = (i+1,j-1)
    se = (i-1,j+1)
    sw = (i-1,j-1)
    n = (i+1,j)
    s = (i-1,j)
    e = (i,j+1)
    w = (i,j-1)
    a = adj[0]
    na = adj[1]
    ca = adj[2]
    if n in a and e in a and ne not in ca:
        corners+=1
    if n in a and w in a and nw not in ca:
        corners+=1
    if s in a and e in a and se not in ca:
        corners+=1
    if s in a and w in a and sw not in ca:
        corners+=1
    if n in na and e in na:
        corners+=1
    if n in na and w in na:
        corners+=1
    if s in na and e in na:
        corners+=1
    if s in na and w in na:
        corners+=1
    return corners


for region, rs in regiondict.items():
    # N S E W
    walls = 0
    for edge in rs:
        if edge in edges_visited:
            continue
        walls+=is_corner(edge[0],edge[1])
    loc = region
    totalprice2+=walls*areadict[region]

for i in range(len(regionmap)):
    printstr = ""
    for j in range(len(regionmap[i])):
        if (i,j) in edges_visited:
            printstr += str(regionmap[i][j])
        else:
            printstr += "."



print("Part 1: " + str(totalprice))
print("Part 2: " + str(totalprice2))
