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
count = 0
done = np.zeros((H,W), 'uint8')

def floodfill(x,y):
    if (map[y][x] == 9): return 0
    if (done[y][x] == 1): return 0
    done[y][x] = 1
    sum = 1
    if x > 0: sum += floodfill(x-1,y)
    if y > 0: sum += floodfill(x,y-1)
    if x < W-1: sum += floodfill(x+1,y)
    if y < H-1: sum += floodfill(x,y+1)
    return sum

sizes = []
for y in range(H):
    for x in range(W):
        if map[y][x] < 9 and done[y][x] == 0:
            size = floodfill(x,y)
            print(size)
            sizes.append(size)
sizes.sort(reverse=True)
slist = sizes
print(slist[0], slist[1], slist[2], slist[0]*slist[1]*slist[2])
