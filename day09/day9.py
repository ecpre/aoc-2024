import sys, time

if len(sys.argv) < 2:
    print("must have argument")
    exit

ifile = open(sys.argv[1], 'r')

blockmap = []

free = False
fid = 0

line = ifile.readline()
linecontent = line.strip()

def get_free_blocks(bmap):
    freeblocks = []
    for i in range(len(bmap)):
        if bmap[i] == " ":
            freeblocks.append(i)
    return freeblocks

def get_free_blocks_p2(bmap):
    freeblocks = []
    i = 0
    while i < len(bmap):
        lastindex = i
        index = i
        if bmap[i] != " ":
            i+=1
            continue
        while True:
            if i > len(bmap)-1:
                break
            elif bmap[i] != " ":
                break
            else:
                lastindex = i
                i+=1
        freeblocks.append([index, lastindex+1])
    return freeblocks

def last_real_block(bmap):
    for i in range(len(bmap)-1, -1, -1):
        if bmap[i] != " ":
            return i
    return None

def get_files(bmap):
    files = []
    i = len(bmap)-1
    while i > -1:
        lastindex = i+1
        index = i
        fid_local = bmap[i]
        if fid_local == " ":
            i-=1
            continue
        while True:
            if i < 0:
                break
            elif bmap[i] != fid_local:
                break
            else:
                index = i
                i-=1
        files.append([index, lastindex])
    return files

for i in range(len(linecontent)):
    if not free:
        blockmap.extend([str(fid)] * int(linecontent[i]))
        fid+=1
    else:
        blockmap.extend([" "] * int(linecontent[i]))

    free = not free

notdone = False

p1blockmap = blockmap.copy()
freeblocks = get_free_blocks(p1blockmap)

def freespaceoptimize():
    global freeblocks
    lastfree = 0
    for freeblock in freeblocks:
        last_block = last_real_block(p1blockmap)
        if last_block != None and lastfree != last_block:
            lastfree = freeblock
            p1blockmap[freeblock] = p1blockmap[last_block]
            p1blockmap[last_block] = " "
    # horribly unoptimized compared to part 2
    nfreeblocks = get_free_blocks(p1blockmap)
    if nfreeblocks[0]-1 == last_real_block(p1blockmap):
        return True
    freeblocks = nfreeblocks
    return False

while freespaceoptimize() == False:
    pass

p2blockmap = blockmap.copy()
freeblocks = get_free_blocks_p2(p2blockmap)

files = get_files(p2blockmap)

def defrag():
    global freeblocks
    global files
    i = 0
    for file in files:
        filelen = file[1]-file[0]
        for freeblock in freeblocks:
            if filelen > freeblock[1]-freeblock[0] or file[0] < freeblock[1]:
                continue
            p2blockmap[freeblock[0]:freeblock[0]+filelen] = p2blockmap[file[0]:file[1]]
            p2blockmap[file[0]:file[1]] = " " * filelen
            file[0] = freeblock[0]
            file[1] = freeblock[0]+filelen
            freeblock[0] = freeblock[0]+filelen
            freeblock[1] = freeblock[1]
            break

defrag()

p1checksum = 0
p2checksum = 0

for i in range(len(blockmap)):
    if p1blockmap[i] != " ":
        p1checksum += i*int(p1blockmap[i])

for i in range(len(p2blockmap)):
    if p2blockmap[i] != " ":
        p2checksum += i*int(p2blockmap[i])

print("Part 1: " + str(p1checksum))
print("Part 2: " + str(p2checksum))
