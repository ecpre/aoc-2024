import sys

if len(sys.argv) < 2:
    print("must have an argument")
    exit

ifile = open(sys.argv[1], 'r')

visitedp1 = set()
gpolemap = []

start_pos = ()
current_dir = []
start_dir = []

row = 0


while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    for i in range(len(linecontent)):
        if linecontent[i] != '.' and linecontent[i] != '#':
            start_pos = (row, i)
            llist = list(linecontent)
            llist[i] = '.'
            if linecontent[i] == '^':
                start_dir = [-1,0]
            elif linecontent[i] == 'v':
                start_dir = [1,0]
            elif linecontent[i] == '>':
                start_dir = [0,1]
            elif linecontent[i] == '<':
                start_dir = [0,-1]
            linecontent = ''.join(llist)

    gpolemap.append(linecontent)
    row+= 1
    
def validate(polemap, p2):
    current_dir = start_dir.copy()
    visitedpv = set()
    cyclepoints = set()
    row = start_pos[0]
    col = start_pos[1]
    while True:
        #print(str((col, row)) + " " + str((current_dir)))
        if ((row, col), tuple(current_dir)) in cyclepoints and p2:
            return True
        visitedpv.add((row, col))
        if row+current_dir[0] >= len(polemap) or row+current_dir[0] < 0 or col+current_dir[1] >= len(polemap[1]) or col+current_dir[1] < 0:
            break
        if polemap[row+current_dir[0]][col+current_dir[1]] == '.':
            row += current_dir[0]
            col += current_dir[1]
        else:
            cyclepoints.add(((row, col), tuple(current_dir)))
            if (current_dir[0] == 0):
                current_dir[0] = current_dir[1]
                current_dir[1] = 0
            elif (current_dir[1] == 0):
                current_dir[1] = -current_dir[0]
                current_dir[0] = 0
    if p2:
        return False
    return visitedpv

visited = validate(gpolemap, False)

p2sum = 0
#brute force!
for i in range(len(gpolemap)):
    for j in range(len(gpolemap[i])):
        if gpolemap[i][j] != '#':
            newpolemap = gpolemap.copy()
            npl = list(newpolemap[i])
            npl[j] = '#'
            npstr = ''.join(npl)
            newpolemap[i] = npstr
            if validate(newpolemap, True):
                p2sum+=1
                print(i)


print("p1: ", str(len(visited)))
print("p2: ", str(p2sum))
