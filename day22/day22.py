import sys
from collections import deque

if len(sys.argv) < 2:
    print("must have argument")
    exit()

ifile = open(sys.argv[1], 'r')

secrets = []

def mix(secret, given):
    return secret ^ given

def prune(secret):
    return secret%16777216

def calculate_next(secret):
    given_1 = secret*64
    secret = mix(secret, given_1)
    secret = prune(secret)
    given_2 = secret // 32
    secret = mix(secret, given_2)
    secret = prune(secret)
    given_3 = secret*2048
    secret = mix(secret, given_3)
    secret = prune(secret)
    return secret

while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    secrets.append(int(line))

secret_sum = 0
master_sequences = {}
for secret in secrets:
    sequences = {}
    sequence = deque(maxlen=4)
    price = secret%10
    secret = calculate_next(secret)
    newprice = secret%10
    sequence.append(newprice-price)
    price = newprice
    secret = calculate_next(secret)
    newprice = secret%10
    sequence.append(newprice-price)
    price = newprice
    secret = calculate_next(secret)
    newprice = secret%10
    sequence.append(newprice-price)
    price = newprice
    secret = calculate_next(secret)
    newprice = secret%10
    sequence.append(newprice-price)
    price = newprice
    print(sequence)
    for i in range(1996):
        secret = calculate_next(secret)
        newprice = secret%10
        sequence.append(newprice-price)
        price = newprice
        if tuple(sequence) not in sequences:
            sequences[tuple(sequence)] = secret % 10
            if tuple(sequence) in master_sequences:
                master_sequences[tuple(sequence)] += secret%10
            else:
                master_sequences[tuple(sequence)] = secret%10

#assuming it exists. may not
best = master_sequences[(-1,-1,0,2)]
for key,val in master_sequences.items():
    if val > best:
        print(val, best)
        best = val
print(secret_sum)
print(best)


