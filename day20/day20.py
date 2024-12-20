import sys

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

racetrack = []
start = (0,0)
end = (0,0)

linenum = 0

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    racetrack.append(linecontent)

    for i in range(len(linecontent)):
        if linecontent[i] == "S":
            start = (linenum, i)
        elif linecontent[i] == "E":
            end = (linenum, i)

    linenum+=1

#could make this a single list, but slightly simpler not to
visited = []
counts = []

def get_next(pos):
    i = pos[0]
    j = pos[1]
    nextpos = (-1,-1)
    if i > 0 and racetrack[i-1][j] != "#" and (i-1,j) not in visited:
        nextpos = (i-1,j)
    elif j > 0 and racetrack[i][j-1] != "#" and (i,j-1) not in visited:
        nextpos = (i,j-1)
    elif i < len(racetrack)-1 and racetrack[i+1][j] != "#" and (i+1,j) not in visited:
        nextpos = (i+1,j)
    elif j < len(racetrack[i])-1 and racetrack[i][j+1] != "#" and (i,j+1) not in visited:
        nextpos = (i,j+1)
    return nextpos

def get_cheat_ends(pos):
    i = pos[0]
    j = pos[1]
    ends = []
    if i > 1 and racetrack[i-1][j] == "#" and (i-2,j) in visited:
        ends.append((i-2,j))
    if j > 1 and racetrack[i][j-1] == "#" and (i,j-2) in visited:
        ends.append((i,j-2))
    if i < len(racetrack)-2 and racetrack[i+1][j] == "#" and (i+2,j) in visited:
        ends.append((i+2,j))
    if j < len(racetrack[i])-2 and racetrack[i][j+1] == "#" and (i,j+2) in visited:
        ends.append((i,j+2))
    return ends

saved_dict_p2 = {}
def get_ends_p2(pos):
    pos_index = visited.index(pos)
    pos_count = counts[pos_index]
    i = pos[0]
    j = pos[1]

    for v in visited:
        manhattan = abs(v[0]-i)+abs(v[1]-j)
        if manhattan <= 20:
            v_index = visited.index(v)
            v_count = counts[v_index]
            saved = v_count - pos_count - manhattan
            if saved > 0 and saved in saved_dict_p2:
                saved_dict_p2[saved]+=1
            elif saved > 0:
                saved_dict_p2[saved]=1

current = start
count = 0
while True:
    visited.append(current)
    counts.append(count)
    if current == end or current == (-1,-1):
        break
    current = get_next(current)
    count+=1

saved_dict = {}
save_100 = 0

for i in range(len(visited)):
    count = counts[i]
    current = visited[i]
    cheat_ends = get_cheat_ends(current)
    get_ends_p2(current)
    for end in cheat_ends:

        endindex = visited.index(end)
        endcount = counts[endindex]
        diff = endcount-count
        saved = diff-2
        if saved >= 100:
            save_100 +=1
        if saved > 0 and saved in saved_dict:
            saved_dict[saved]+=1
        elif saved > 0:
            saved_dict[saved]=1

print("Part 1: " + str(save_100))
save_100_p2 = 0
for key in saved_dict_p2:
    if key >= 100:
        save_100_p2 += saved_dict_p2[key]

print("Part 2: " + str(save_100_p2))
