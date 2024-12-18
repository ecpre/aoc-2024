import sys, collections

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

tofall = []
fallen = set()
explored = set()
start = (0,0)
end = (70,70)

def get_adjacent(i,j):
    adjacent = []
    if i > 0 and (i-1,j) not in fallen:
        adjacent.append((i-1,j))
    if j > 0 and (i,j-1) not in fallen:
        adjacent.append((i,j-1))
    if i < end[0] and (i+1,j) not in fallen:
        adjacent.append((i+1, j))
    if j < end[0] and (i,j+1) not in fallen:
        adjacent.append((i,j+1))
    return adjacent

def bfs():
    queue = collections.deque()
    explored.add(start)
    queue.append(((start), None))
    while queue:
        current = queue.popleft()
        if current[0] == end:
            return current
        adj = get_adjacent(current[0][0], current[0][1])
        for a in adj:
            if a not in explored:
                explored.add(a)
                queue.append((a, current))
    return None


while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break
    
    fall = linecontent.split(",")
    tofall.append((int(fall[0]), int(fall[1])))

for i in range(1024):
    if i > len(tofall)-1:
        break
    fallen.add(tofall[i])

endbfs = bfs()
steps = 0

print("Part 1: " + str(steps))

while endbfs[1] is not None:
    steps+=1
    endbfs = endbfs[1]

for i in range(1023, len(tofall)):
    fallen.add(tofall[i])
    explored.clear()
    if bfs() == None:
        print("Part 2: " + str(tofall[i]))
        break

