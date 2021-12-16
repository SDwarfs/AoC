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
#count = 0

path = {
    0: [ [0, 0] ]
}

def findPath(x,y,risk):
    global bestfound
    #count += 1
    #print(x,y,risk)
    #if count > 10: exit()
    left = ((W-1)-x) + ((H-1)-y)
    if (risk + left) > bestfound: return bestfound
    if x == W-1 and y == H-1:
        print("FOUND:", x, y, risk)
        if risk < bestfound:
            bestfound = risk
        return
    # down / right first
    if x<W-1: findPath(x+1, y, risk + map[y][x+1])
    if y<H-1: findPath(x, y+1, risk + map[y+1][x])
    if x>0:   findPath(x-1, y, risk + map[y][x-1])
    if y>0:   findPath(x, y-1, risk + map[y-1][x])

findPath(0,0,0)
print(bestfound)
