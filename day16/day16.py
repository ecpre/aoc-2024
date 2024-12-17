import sys, math

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

maze = []
start = ()
end = ()

def get_adjacent_weights(i,j,direc):
    adjacent = []
    if i > 0 and maze[i-1][j] != "#":
        weight = 1
        if direc != "^":
            weight+=1000
        adjacent.append(((i-1,j),weight,"^"))
    if j > 0 and maze[i][j-1] != "#":
        weight = 1
        if direc != "<":
            weight += 1000
        adjacent.append(((i,j-1),weight,"<"))
    if i < len(maze)-1 and maze[i+1][j] != "#":
        weight = 1
        if direc != "v":
            weight += 1000
        adjacent.append(((i+1,j),weight,"v"))
    if j < len(maze[i])-1 and maze[i][j+1] != "#":
        weight = 1
        if direc != ">":
            weight+=1000
        adjacent.append(((i,j+1),weight,">"))
    return adjacent

def cheapest_path(nodes):
    distances = []
    current = None
    while nodes:
        current = nodes[0]
        for node in nodes:
            if node[1] < current[1]:
                current = node
        if current[1] == math.inf:
            break
        adj = get_adjacent_weights(current[0][0],current[0][1],current[2])
        for a in adj:
            for node in nodes:
                if a[0] == node[0] and a[1]+current[1] < node[1] and a[2] == node[2]:
                    node[1] = a[1]+current[1]
                    node[2] = a[2]
                    node[3].clear()
                    node[3].update(current[3])
                    node[3].add(current[0])
                elif a[0] == node[0] and a[1]+current[1] == node[1] and a[2] == node[2]:
                    node[3].update(current[3])
                    node[3].add(current[0])
        distances.append(current)
        nodes.remove(current)
    return distances
    
while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    maze.append(linecontent)

nodes = []

for i in range(len(maze)):
    for j in range(len(maze[i])):
        node = [(i,j), math.inf, ">", set()]
        exnodes = [node]
        if maze[i][j] == "S":
            start = (i,j)
            node[1] = 0
        else:
            exnodes.append([(i,j), math.inf, "<", set()])
            exnodes.append([(i,j), math.inf, "^", set()])
            exnodes.append([(i,j), math.inf, "v", set()])
        if maze[i][j] == "E":
            end = (i,j)
        if maze[i][j] != "#":
            nodes.extend(exnodes)

distances = cheapest_path(nodes)

endcost = math.inf
endnode = None
pathnodes = set()
for dist in distances:
    if dist[0] == end:
        if dist[1] < endcost:
            endcost = dist[1]
            endnode = [dist]
            pathnodes.update(dist[3])
        elif dist[1] == endcost:
            endnode.append(dist)
            pathnodes.update(dist[3])
        
print("Part 1: " + str(endcost))

print("Part 2: " + str(len(pathnodes)+1))
