import sys, math

if len(sys.argv) < 2:
    print("must have argument")
    exit

ifile = open(sys.argv[1], 'r')

antennaemap = []
antinodes = set()
antennae = {}

linenum = 0

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break
    
    antennaemap.append(linecontent)

    for i in range(len(linecontent)):
        if linecontent[i] != '.':
            if linecontent[i] in antennae:
                antennae[linecontent[i]].append((linenum, i))
            else:
                antennae[linecontent[i]] = [(linenum, i)]
    
    linenum+=1

def find_antinodes(p2):
# four nested fors? uh oh... 
# not that bad actually!
    for i in range(len(antennaemap)):
        for j in range(len(antennaemap[i])):
            found = False
            for freq in antennae.values():
                distances = set()
                for loc in freq:
                    if loc == (i, j) and len(freq)>1 and p2:
                        antinodes.add((i,j))
                        found = True
                        break
                    locdist = 0
                    if not p2:
                        locdist = math.dist((i,j), loc)
                    slope = 9999999
                    if j != loc[1]:
                        slope = (i-loc[0])/(j-loc[1])
                    if (locdist*2, slope) in distances or (locdist/2, slope) in distances:
                        antinodes.add((i,j))
                        found = True
                    distances.add((locdist, slope))
                    if found:
                        break
                if found:
                    break

find_antinodes(False)
print("Part 1: " + str(len(antinodes)))
antinodes = set()
find_antinodes(True)
print("Part 2: " + str(len(antinodes)))
