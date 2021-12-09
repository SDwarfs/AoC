import numpy as np

def parse(line):
    return [[int(i) for i in j.split(",")] for j in line.rstrip().split(" -> ")]

lines = [parse(x) for x in open("input.txt")]
MAXX = 1000
MAXY = 1000

map = np.zeros((MAXX,MAXY), 'int')
for (p1,p2) in lines:
    vec = [p2[0]- p1[0], p2[1]-p1[1]]
    len = max(abs(vec[0]), abs(vec[1]))
    if len > 0:
        dir = [int(vec[0]/len), int(vec[1]/len)]
    else:
        dir = [0, 0]
    #print(p1, p2, ", VEC:", vec, ", DIR:", dir, ", LEN: ", len, end=" -> ")
    for i in range(len+1):
        x = p1[0] + dir[0]*i
        y = p1[1] + dir[1]*i
        map[y][x] += 1
    #print("")
    #print((x,y), end="  ")
count = 0
for x in range(MAXX):
    for y in range(MAXY):
        if map[y][x] > 1:
            count += 1
#print(map)
print(count)
exit()
