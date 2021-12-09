import numpy as np

def parse(line):
    return [[int(i) for i in j.split(",")] for j in line.rstrip().split(" -> ")]

lines = [parse(x) for x in open("sample.txt")]
MAXX = 10
MAXY = 10

map = np.zeros((MAXX,MAXY), 'int')
for (p1,p2) in lines:
    if p1[0] == p2[0]:
        x = p1[0]
        y1 = min(p1[1], p2[1])
        y2 = max(p1[1], p2[1])
        for y in range(y1,y2+1): map[y][x] +=1
    elif p1[1] == p2[1]:
        y = p1[1]
        x1 = min(p1[0], p2[0])
        x2 = max(p1[0], p2[0])
        for x in range(x1,x2+1): map[y][x] +=1
    else:
        pass
        #print("ERROR")
        #exit()
count = 0
for x in range(MAXX):
    for y in range(MAXY):
        if map[y][x] > 1:
            count += 1
print(map)
print(count)
exit()
