import sys, copy

if len(sys.argv) < 4:
    print("must have arguments")
    exit()

ifile = open(sys.argv[1], 'r')

xdim = int(sys.argv[2])
ydim = int(sys.argv[3])

halfx = xdim//2
halfy = ydim//2

robots = []

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    robotstrs = linecontent.split(" ")

    robotposstr = robotstrs[0][2:].split(",")
    robotpos = [int(x) for x in robotposstr]

    robotvelstr = robotstrs[1][2:].split(",")
    robotvel = [int(x) for x in robotvelstr]

    robots.append([robotpos, robotvel])

timer = 0

rob = robots[0]

robots100 = []

while timer < xdim*ydim:
    
    locset = set()
    dup = False

    for robot in robots:
        # guessing there won't be any overlap. probably not true for all cases
        # but it worked, so it's fine
        pos = robot[0]
        vel = robot[1]

        if tuple(pos) in locset:
            dup = True
        else: 
            locset.add(tuple(pos))

        pos[0] = (pos[0]+vel[0])%(xdim)
        pos[1] = (pos[1]+vel[1])%(ydim)
    
    timer+=1
    if not dup:
        print(str(timer) + ": ")
        for y in range(ydim):
            printstr = ""
            for x in range(xdim):
                if (x,y) in locset:
                    printstr += "█"
                else:
                    printstr += "▓"
            print(printstr)

    if timer == 100:
        robots100 = copy.deepcopy(robots)

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for robot in robots100:
    if robot[0][0] < halfx:
        if robot[0][1] < halfy:
            q1+=1
        elif robot[0][1] > halfy:
            q2+=1
    elif robot[0][0] > halfx:
        if robot[0][1] < halfy:
            q3+=1
        elif robot[0][1] > halfy:
            q4+=1

print("Part 1: " + str(q1*q2*q3*q4))
print("Part 2: go find it")
