import numpy as np

# read all input lines into lines[] and strip off trailing whitespaces
lines = [x.rstrip() for x in open("input.txt")]

map = []
for line in lines:
    if line == "": continue
    map.append([int(x) for x in line])

H = len(map)
W = len(map[0])

bestfound = H*W*10

path = { }

def getLeft(x,y):
    global H, W
    return ((W-1)-x) + ((H-1)-y)

bestfound = np.zeros((H,W), 'int')
bestfound[:] = H*W*10

def addPosition(x,y,cost):
    global path, bestfound
    cost += map[y][x]
    cost_min = cost + getLeft(x,y)
    if bestfound[y][x] < cost_min: return
    bestfound[y][x] = cost_min
    if not cost_min in path:
        path[cost_min] = []
    path[cost_min].append([x, y, cost])
    #print("NEW:", path)


addPosition(0,0,-map[0][0])

while True:
    next = min(path.keys())
    next_positions = path.pop(next)
    #print("NEXT: ", next, next_positions)
    print(next)
    for pos in next_positions:
        (x,y, cost) = pos
        if x == H-1 and y == W-1:
            bestrisk = cost
            print("BESTRISK:", bestrisk)
            exit()
        if x<W-1: addPosition(x+1, y, cost)
        if y<H-1: addPosition(x, y+1, cost)
        if x>0:   addPosition(x-1, y, cost)
        if y>0:   addPosition(x, y-1, cost)

        #exit()
