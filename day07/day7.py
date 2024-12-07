import sys, itertools

if len(sys.argv) < 2:
    print("must have an argument")
    exit

ifile = open(sys.argv[1], 'r')

p1sum = 0
p2sum = 0

def investigate(linesplit, opsum, ops):
    retval = 0
    tmpsplit = linesplit.copy()
    for x in itertools.product(ops, repeat=len(linesplit)-2):
        j = 0
        workingsum = int(tmpsplit[1])
        for i in range(2, len(tmpsplit)):
            if (x[j] == '+'):
                workingsum += int(tmpsplit[i])
            elif (x[j] == '*'):
                workingsum *= int(tmpsplit[i])
            elif (x[j] == 'c'):
                wsumstr = str(workingsum)
                wsumstr+= tmpsplit[i]
                workingsum = int(wsumstr)
            j+=1
        if workingsum == opsum:
            retval += opsum
            break
    return retval

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    linesplit = linecontent.split(' ')
    opsum = int(linesplit[0][:-1])

    p1sum += investigate(linesplit, opsum, "+*")
    p2sum += investigate(linesplit.copy(), opsum, "+*c")


print("p1: ", str(p1sum))
print("p2: ", str(p2sum))
