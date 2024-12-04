# note to self .maybe next year make some helper functions in library

import sys
import collections
if len(sys.argv) < 2:
    print("must have an argument")
    exit

ifile = open(sys.argv[1], 'r')

wordsearch = []
xmascnt = 0

def search_diag():
    pass

#not the prettiest code I have written...
#but it does work
#and easier than the first part since i didn't have
#to work on all my search helper functions
#oh well
#not the most optimal either
def findxs():
    cnt=0
    for i in range(1, len(wordsearch)-1):
        for j in range(1, len(wordsearch[i])-1):
            if wordsearch[i][j] == 'A':
                if (((wordsearch[i-1][j-1] == 'M' and wordsearch[i+1][j+1] == 'S') 
                or (wordsearch[i-1][j-1] == 'S' and wordsearch[i+1][j+1] == 'M'))
                and ((wordsearch[i+1][j-1] == 'M' and wordsearch[i-1][j+1] == 'S')
                     or (wordsearch[i+1][j-1] == 'S' and wordsearch[i-1][j+1] == 'M'))):
                    cnt+=1
    return cnt

def search_topbtm():
    global xmascnt
    for j in range(len(wordsearch[0])):
        buf = []
        for i in range(len(wordsearch)):
            buf.append(wordsearch[i][j])
        bufstr = "".join(buf)
        print(bufstr)
        xmascnt += bufstr.count("XMAS") + bufstr.count("SAMX")

def search_diag_up():
    global xmascnt
    i = 0
    while i < len(wordsearch):
        itmp = i
        j = 0
        buf = []
        while itmp >= 0 and j < len(wordsearch[i]):
            buf.append(wordsearch[itmp][j])
            itmp-=1
            j+=1
        bufstr = "".join(buf)
        #print(bufstr)
        xmascnt += bufstr.count("XMAS") + bufstr.count("SAMX")
        i+=1
    j=1
    # ugly. code repetition unncessary but oh well
    while j < len(wordsearch[0]):
        jtmp = j
        i = len(wordsearch)-1
        buf = []
        while jtmp < len(wordsearch[i]) and i < len(wordsearch):
            buf.append(wordsearch[i][jtmp])
            jtmp+=1
            i-=1
        bufstr = "".join(buf)
        xmascnt += bufstr.count("XMAS") + bufstr.count("SAMX")
        #print(bufstr)
        j+=1


def search_diag_down():
    global xmascnt
    i = 0
    while i < len(wordsearch):
        itmp = i
        j = 0
        buf = []
        while itmp <len(wordsearch) and j < len(wordsearch[i]):
            buf.append(wordsearch[itmp][j])
            itmp+=1
            j+=1
        bufstr = "".join(buf)
        xmascnt += bufstr.count("XMAS") + bufstr.count("SAMX")
        i+=1
    j = 1
    # ugly
    while j < len(wordsearch[0]):
        jtmp = j
        i = 0
        buf = []
        while jtmp < len(wordsearch[i]) and i < len(wordsearch):
            buf.append(wordsearch[i][jtmp])
            jtmp+=1
            i+=1
        bufstr = "".join(buf)
        xmascnt += bufstr.count("XMAS") + bufstr.count("SAMX")
        j+=1


while True:
    line = ifile.readline()
    linecontent = line.strip()

    if not line:
        break

    wsearchline = list(linecontent)
    wordsearch.append(wsearchline)

    xmascnt+=linecontent.count("XMAS")+linecontent.count("SAMX")

search_topbtm()
search_diag_up()
search_diag_down()

print("Part 1: " + str(xmascnt))
print("Part 2: " + str(findxs()))
