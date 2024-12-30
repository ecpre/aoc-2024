import sys

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

readinputs = True

inputs = {}
operations = []
prev = {}

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    if linecontent == "":
        readinputs = False
        continue

    if readinputs:
        linesplit = linecontent.split(" ")
        inputs[linesplit[0][:-1]] = int(linesplit[1])
        prev[linesplit[0][:-1]] = []

    else:
        linesplit = linecontent.split(" ")
        operations.append([linesplit[0],linesplit[1],linesplit[2],linesplit[4], False])

solved = False

while not solved:
    solved = True
    for op in operations:
        if op[0] not in inputs or op[2] not in inputs:
            continue
        print(op)
        # if begins with z
        if not op[4]:
            prev[op[3]] = [op[0],op[1],op[2]]
            solved = False
        res = 0
        match op[1]:
            case "AND":
                res = inputs[op[0]] & inputs[op[2]]
            case "OR":
                res = inputs[op[0]] | inputs[op[2]]
            case "XOR":
                res = inputs[op[0]] ^ inputs[op[2]]
        inputs[op[3]] = res
        op[4] = True

binaryx = ""
binaryy = ""
binaryz = ""
inputs = dict(sorted(inputs.items()))
for key, value in inputs.items():
    if key[0] == "z":
        binaryz+=str(value)
    elif key[0] == "x":
        binaryx+=str(value)
    elif key[0] == "y":
        binaryy+=str(value)

binzdec = int(binaryz[::-1],2)
expected = int(binaryx[::-1],2)+int(binaryy[::-1],2)

expectedstr = str(bin(expected))[::-1][:-2]

print(binaryz)
print(expectedstr)

print(len(binaryz))
print(len(expectedstr))

print(prev["z01"])

def print_prev(zstr, depth):
    if depth == 0:
        return
    if prev[zstr] == []:
        print(zstr)
        return
    print(zstr, "=", prev[zstr])
    print_prev(prev[zstr][0], depth-1)
    print_prev(prev[zstr][2], depth-1)

for i in range(len(expectedstr)):
    if expectedstr[i] != binaryz[i]:
        print("mismatch", i)
        zstr = "z" + str(i).zfill(2)
        prevdepth = [zstr]

        print_prev(zstr, 5)


print("Part 1: ", binzdec)

