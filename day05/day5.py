import sys

if len(sys.argv) < 2:
    print("must have an argument")
    exit

ifile = open(sys.argv[1], 'r')

rules = []
valid = []
invalid = []

rulesearch = True

#ugly impl
def validate_order(order, swap):
    for rule in rules:
        already = set()
        for page in order:
            page = int(page)
            if page == rule[0] and rule[1] in already:
                if not swap:
                    return False
                i1 = order.index(str(rule[0]))
                i2 = order.index(str(rule[1]))
                tmp = order[i1]
                order[i1] = order[i2]
                order[i2] = tmp
                #ugly recursion oh no. supri
                return validate_order(order, swap)
            already.add(page)
    if swap:
        return order
    return True

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break
    
    if linecontent == "":
        rulesearch = False
        continue
    
    if rulesearch:
        rulesplit = linecontent.split('|')
        rules.append([int(rulesplit[0]), int(rulesplit[1])])
    else:
        order = linecontent.split(',')
        if validate_order(order, False):
            valid.append(order)
        else:
            invalid.append(validate_order(order, True))

p1sum = 0
p2sum = 0
for i in range(len(valid)):
    p1sum += int(valid[i][len(valid[i])//2])
for i in range(len(invalid)):
    p2sum += int(invalid[i][len(invalid[i])//2])

print("Part 1: " + str(p1sum))
print("Part 2: " + str(p2sum)) 
