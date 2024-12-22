import sys
from functools import cache

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

#evil coordinate system where 0,0 is empty space
positions = [(1,0), (0,-1), (1,-1),
             (2,-1), (0,-2), (1,-2),
             (2,-2), (0,-3), (1,-3),
             (2,-3), (2,0)]

directions = {"^": (1,0), "A": (2,0), "<": (0,1), "v": (1,1), ">": (2,1)}

@cache
def get_sequence(move, presses, init_mov, depth, directional):
    new = None
    init = None
    if depth == 0:
        return presses

    if directional:
        init = directions[init_mov]
        new = directions[move]
    else:
        init = positions[init_mov]
        new = positions[move]
    diff_i = init[1]-new[1]
    diff_j = init[0]-new[0]
    
    length = 0

    if diff_i > 0:
        mov_i = ("^", diff_i)
    else:
        mov_i = ("v", abs(diff_i))
    if diff_j > 0:
        mov_j = ("<", diff_j)
    else:
        mov_j = (">", abs(diff_j))

    if diff_i == 0:
        length+=(get_sequence(mov_j[0], mov_j[1], "A"     , depth-1, True) +
                 get_sequence("A"     , presses , mov_j[0], depth-1, True))
    elif diff_j == 0:
        length+=(get_sequence(mov_i[0], mov_i[1], "A"     , depth-1, True) +
                 get_sequence("A"     , presses , mov_i[0], depth-1, True))
    elif ((init[0] == 0 and new[1] == 0) or diff_j > 0) and not (init[1] == 0 and new[0] == 0):
        length+=(get_sequence(mov_j[0], mov_j[1], "A"     , depth-1, True) +
                 get_sequence(mov_i[0], mov_i[1], mov_j[0], depth-1, True) +
                 get_sequence("A"     , presses , mov_i[0], depth-1, True))
    else:
        length+=(get_sequence(mov_i[0], mov_i[1], "A"     , depth-1, True) +
                 get_sequence(mov_j[0], mov_j[1], mov_i[0], depth-1, True) +
                 get_sequence("A"     , presses , mov_j[0], depth-1, True))

    return length

sum_complexity = 0
sum_complexity_p1 = 0
for code in codes:
    complexity = 0
    complexity_p1 = 0
    for i in range(len(code)):
        complexity += get_sequence(int(code[i], 16), 1, int(code[i-1], 16), 26, False)
        complexity_p1 += get_sequence(int(code[i], 16), 1, int(code[i-1], 16), 3, False)
    sum_complexity += complexity * int(code[:len(code)-1])
    sum_complexity_p1 += complexity_p1 * int(code[:len(code)-1])

print("Part 1: " + str(sum_complexity_p1))
print("Part 2: " + str(sum_complexity))
