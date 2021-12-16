import numpy as np
from time import time
# read all input lines into lines[] and strip off trailing whitespaces
lines = [x.rstrip() for x in open("input.txt")]

map = []
for line in lines:
    if line == "": continue
    map.append([int(x) for x in line])

def extendMap(map, factor = 5):
    H_ = len(map)
    W_ = len(map[0])
    W=W_*factor
    H=H_*factor
    new_map = np.zeros((H, W), 'int')
    for dy in range(factor):
        for y in range(H_):
            for dx in range(factor):
                for x in range(W_):
                    orig = map[y][x]
                    wrap = (dx+dy + orig-1) % 9 + 1
                    new_map[y + dy*H_][x + dx*W_] = wrap

    return new_map

map = extendMap(map, 5)
(H,W) = map.shape
bestfound = H*W*10
path = { }

def getLeft(x,y):
    global H, W
    return ((W-1)-x) + ((H-1)-y)

bestfound = np.zeros((H,W), 'int')
bestfound[:] = H*W*10
done = np.zeros((H,W), 'uint8')

def addPosition(x,y,cost):
    global path, bestfound
    if done[y][x] > 0: return
    cost += map[y][x]
    cost_min = cost + getLeft(x,y)
    if bestfound[y][x] <= cost_min: return
    bestfound[y][x] = cost_min
    if not cost_min in path:
        path[cost_min] = []
    path[cost_min].append([x, y, cost])

addPosition(0,0,-map[0][0])


originalLeft = getLeft(0,0)
lastReport = 0
while True:
    next = min(path.keys())
    next_positions = path.pop(next)
    if time() > lastReport+1:
        currentLeft = getLeft(next_positions[0][0], next_positions[0][1])
        percent_done = round(100*(originalLeft-currentLeft)/originalLeft*10)/10
        print("\r", percent_done, "%", end='    ')
        lastReport = time()
    for pos in next_positions:
        (x, y, cost) = pos
        if x == H-1 and y == W-1:
            bestrisk = cost
            print("\nBESTRISK:", bestrisk)
            exit()
        done[y][x] = 1
        if x<W-1: addPosition(x+1, y, cost)
        if y<H-1: addPosition(x, y+1, cost)
        if x>0:   addPosition(x-1, y, cost)
        if y>0:   addPosition(x, y-1, cost)
