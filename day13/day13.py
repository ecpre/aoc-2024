import sys

if len(sys.argv) < 2:
    print("must have an argument")
    exit

ifile = open(sys.argv[1], 'r')
additional = 0
if len(sys.argv) > 2:
    additional = int(sys.argv[2])

totalcost = 0

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    if line == "\n":
        continue

    al = linecontent[10:].split(", ")
    linecontent = ifile.readline().strip()
    bl = linecontent[10:].split(", ")
    linecontent = ifile.readline().strip()
    prizel = linecontent[7:].split(", ")
    
    a = [int(x[2:]) for x in al]
    b = [int(x[2:]) for x in bl]
    prize = [int(x[2:])+additional for x in prizel]
    
    bsol = ((prize[1]*a[0])-(a[1]*prize[0]))/(-a[1]*b[0]+b[1]*a[0])
    asol = ((prize[0]-bsol*b[0])/a[0])
    if asol < 0 or bsol < 0 or not asol.is_integer() or not bsol.is_integer():
        continue
    cost = asol*3 + bsol
    totalcost+=cost

print(totalcost)
