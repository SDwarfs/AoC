import numpy as np

lines = [x.rstrip() for x in open("input.txt")]
#print(lines)
H = len(lines)
W = len(lines[0])
map = []
for y in range(H):
    if len(lines[y])==0:
        H = y
        break
    line = []
    for x in range(W):
        line.append(int(lines[y][x]))
    map.append(line)
W = len(map[0])
H = len(map)
print(W, H)
count = 0
for y in range(H):
    for x in range(W):
        ok = True
        cur = map[y][x]
        #print(x,y,cur, end="|")
        if x > 0 and map[y][x-1]<=cur:
            ok = False
        if x < W-1 and map[y][x+1]<=cur:
            ok = False
        if y > 0 and map[y-1][x]<=cur:
            ok = False
        if y < H-1 and map[y+1][x]<=cur:
            ok = False
        if ok:
            count += 1 + int(cur)
            print(x,y,"->", cur)
print("END")
print(count)
