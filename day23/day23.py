import sys

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

setdict = {}

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    comps = linecontent.split("-")
    if comps[0] not in setdict:
        setdict[comps[0]] = [comps[1]]
    else:
        setdict[comps[0]].append(comps[1])
    if comps[1] not in setdict:
        setdict[comps[1]] = [comps[0]]
    else:
        setdict[comps[1]].append(comps[0])

triples = []
all_connected = []
for key, value in setdict.items():
    connected = {key}
    for comp in value:
        for comp2 in value:
            if comp == comp2:
                continue
            if comp2 in setdict[comp]:
                triple_set = {key, comp, comp2}
                if triple_set not in triples:
                    triples.append(triple_set)
        conned = True
        for comp2 in connected:
            if comp2 not in setdict[comp]:
                conned = False
        if conned:
            connected.add(comp)
    all_connected.append(connected)


cont_t = 0
for triple in triples:
    for comp in triple:
        if comp[0] == "t":
            cont_t+=1
            break

print("Part 1:", str(cont_t))


print("Part 2:", ",".join(sorted(max(all_connected, key=len))))

