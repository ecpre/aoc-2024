import sys

if len(sys.argv) < 2:
    print("must have arguments")
    exit()

ifile = open(sys.argv[1], 'r')

linecontent = ifile.readline().strip()
reg_a = int(linecontent.split()[2])

linecontent = ifile.readline().strip()
reg_b = int(linecontent.split()[2])

linecontent = ifile.readline().strip()
reg_c = int(linecontent.split()[2])

ifile.readline()

reg_a_init = reg_a
reg_b_init = reg_b
reg_c_init = reg_c

linecontent = ifile.readline().strip()
program = [int(x) for x in linecontent.split()[1].split(",")]

pc = 0
output = []


def combo(operand):
    if operand <= 3:
        return operand
    match operand:
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c

def adv(operand):
    global reg_a
    reg_a //= (2**combo(operand))

def bxl(operand):
    global reg_b
    reg_b ^= operand

def bst(operand):
    global reg_b
    reg_b = combo(operand)%8

def jnz(operand):
    global pc
    if reg_a == 0:
        return
    else:
        pc = operand-2

def bxc(operand):
    global reg_b
    global reg_c
    reg_b ^= reg_c
    
def out(operand):
    output.append(combo(operand)%8)

def bdv(operand):
    global reg_b
    global reg_a
    reg_b = reg_a // 2**combo(operand)

def cdv(operand):
    global reg_c
    global reg_a
    reg_c = reg_a // 2**combo(operand)

opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

while pc < len(program):
    opcodes[program[pc]](program[pc+1])
    pc+=2

print("Part 1: " + ",".join(str(x) for x in output))

newprogout = []

reg_a_init= 0
reg_b_init = 0
reg_c_init = 0
pc = 0
for n in range(1, len(program)):
    # //8 is >> 3
    reg_a_init_2 = reg_a_init << 3
    while True:
        reg_a = reg_a_init_2
        output = []
        pc = 0
        while pc < len(program):
            opcodes[program[pc]](program[pc+1])
            pc+=2
        if output == program[len(program)-1-n:]:
            reg_a_init = reg_a_init_2
            break
        reg_a_init_2+=1

print("Part 2: " + str(reg_a_init))
