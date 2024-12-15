import sys

if len(sys.argv) < 2:
    print("must have arguments")
    exit()

ifile = open(sys.argv[1], 'r')

mapbuilding = True

robotpos = []
robotposp2 = []
walls = []
wallsp2 = []
boxes = []
boxesp2 = []

moves = []

mapline = 0
mapwidth = 0

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    if linecontent == "":
        mapbuilding = False
        continue

    if mapbuilding:
        mapwidth = len(linecontent)
        for i in range(len(linecontent)):
            if linecontent[i] == "#":
                walls.append([mapline,i])
                wallsp2.extend([[mapline,i*2],[mapline,(i*2)+1]])
            elif linecontent[i] == "O":
                boxes.append([mapline,i])
                boxesp2.append([[mapline,i*2],[mapline,(i*2)+1]])
            elif linecontent[i] == "@":
                robotpos = [mapline, i]
                robotposp2 = [mapline, i*2]
        mapline+=1
        continue
    
    moves.extend(list(linecontent))

def printmap():
    for i in range(mapline):
        printstr = ""
        for j in range(mapwidth*2):
            contcond = False
            for box in boxesp2:
                if [i,j] in box:
                    printstr += "O"
                    contcond = True
            if contcond:
                continue
            if [i,j] in wallsp2:
                printstr += "#"
            elif robotposp2 == [i,j]:
                printstr += "@"
            else:
                printstr += "."
        print(printstr)

for move in moves:
    movedir = [0,0]
    ry = robotpos[0]
    rx = robotpos[1]
    
    match move:
        case "^":
            movedir = [-1,0]
        case ">":
            movedir = [0,1]
        case "v":
            movedir = [1,0]
        case "<":
            movedir = [0,-1]

    my = movedir[0]
    mx = movedir[1]

    newpos = [ry+my, rx+mx]

    if newpos in walls:
        continue
    elif newpos in boxes:
        tomove = [boxes.index(newpos)]
        newnewpos = [newpos[0]+my,newpos[1]+mx]
        while newnewpos in boxes:
            tomove.append(boxes.index(newnewpos))
            newnewpos = [newnewpos[0]+my,newnewpos[1]+mx]
        if newnewpos in walls:
            continue
        for boxi in tomove:
            boxes[boxi] = [boxes[boxi][0]+my, boxes[boxi][1]+mx]
    robotpos = newpos
    

for move in moves:
    movedir = [0,0]
    ry = robotposp2[0]
    rx = robotposp2[1]
    match move:
        case "^":
            movedir = [-1,0]
        case ">":
            movedir = [0,1]
        case "v":
            movedir = [1,0]
        case "<":
            movedir = [0,-1]
    
    my = movedir[0]
    mx = movedir[1]

    newpos = [ry+my, rx+mx]

    if newpos in wallsp2:
        continue
    tomove = set()
    newposis = []
    for box in boxesp2:
        if newpos in box:
            tomove.add(boxesp2.index(box))
            newposis.extend([[box[0][0]+my, box[0][1]+mx],
                            [box[1][0]+my, box[1][1]+mx]])
            
    if len(tomove) == 0:
        robotposp2 = newpos
        continue
    j = 0
    wall = False
    while j < len(newposis):
        npos = newposis[j]
        if npos in wallsp2:
            wall = True
            break
        for box in boxesp2:
            if npos in box:
                npos = [-1,-1]
                tomove.add(boxesp2.index(box))
                if [box[0][0]+my, box[0][1]+mx] not in newposis and [box[1][0]+my, box[1][1]+mx] not in newposis:
                    newposis.extend([[box[0][0]+my, box[0][1]+mx],
                                     [box[1][0]+my, box[1][1]+mx]])
        j+=1
    if wall:
        continue
    for boxi in tomove:
        boxesp2[boxi] = [[boxesp2[boxi][0][0]+my, boxesp2[boxi][0][1]+mx],
                        [boxesp2[boxi][1][0]+my, boxesp2[boxi][1][1]+mx]]

    robotposp2 = newpos

totalgps = 0

printmap()

for box in boxes:
    tdist = box[0]
    ldist = box[1]

    gps = 100*tdist + ldist
    totalgps+=gps

totalgps2 = 0

for box in boxesp2:
    tdist = box[0][0]
    ldist = box[0][1]

    gps = 100*tdist + ldist
    totalgps2+=gps

print("Part 1: " + str(totalgps))
print("Part 2: " + str(totalgps2))
