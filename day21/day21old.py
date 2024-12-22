import sys

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

codes = []

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    codes.append(linecontent)

positions = [(3,1), (2,0), (2,1),
             (2,2), (1,0), (1,1),
             (1,2), (0,0), (0,1),
             (0,2), (3,2)]

directions = {"^": (0,1), "A": (0,2), "<": (1,0), "v": (1,1), ">": (1,2)}

def get_sequence(sequence, num, directional):
    retseq = ""
    new = None
    init = None
    if directional:
        init = directions["A"]
        new = directions[num]
        if sequence != "":
            init = directions[sequence[-1]]
    else:
        init = positions[0xa]
        new = positions[num]
        if sequence != "":
            init = positions[int(sequence[-1], 16)]
    diff_i = init[0]-new[0]
    diff_j = init[1]-new[1]
    if (init[1] != 0 and new[1] == 0 and ((init[0] == 3 and not directional) or (init[0] == 0 and directional))) or diff_i < 0 and diff_j < 0:
        print("sotrue")
        for i in range(abs(diff_i)):
            if diff_i > 0:
                retseq+="^"
            elif diff_i < 0:
                retseq+="v"
        for j in range(abs(diff_j)):
            if diff_j > 0:
                retseq+="<"
            elif diff_j < 0:
                retseq+=">"
    else:
    #ordering of these is important
        for j in range(abs(diff_j)):
            if diff_j > 0:
                retseq+="<"
            elif diff_j < 0:
                retseq+=">"
        for i in range(abs(diff_i)):
            if diff_i > 0:
                retseq+="^"
            elif diff_i < 0:
                retseq+="v"
    retseq+="A"
    return retseq

#def get_directional_sequence(sequence, direction):
#    init = directions["A"]
#    new = directions[direction]
#    retseq = ""
#    if sequence != "":
#        init = directions[sequence[-1]]
#    diff_i = init[0]-new[0]
#    diff_j = init[1]-new[1]

sum_complexity = 0

for code in codes:
    seq_rob_1 = ""
    print(code)
    for i in range(len(code)):
        seq_rob_1 += get_sequence(code[:i], int(code[i], 16), False)
    seq_rob_2 = ""
    for i in range(len(seq_rob_1)):
        seq_rob_2 += get_sequence(seq_rob_1[:i], seq_rob_1[i], True)
    seq_final = ""
    for i in range(len(seq_rob_2)):
        seq_final += get_sequence(seq_rob_2[:i], seq_rob_2[i], True)
    print(seq_rob_1)
    print(seq_rob_2)
    print(seq_final)
    print(code[:-1], len(seq_final))
    print("")
    sum_complexity += int(code[:len(code)-1])*len(seq_final)

print(sum_complexity)
