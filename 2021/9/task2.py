import numpy as np

lines = [x.rstrip() for x in open("input.txt")]
map = []
for line in lines:
    if line != "": map.append([int(x) for x in line])
H = len(map)
W = len(map[0])

done = np.full((H,W), False, dtype=bool)

def floodfill(x,y):
    if map[y][x] == 9 or done[y][x] == True: return 0
    done[y][x] = True
    size = 1
    if x > 0:   size += floodfill(x-1, y  )
    if y > 0:   size += floodfill(x,   y-1)
    if x < W-1: size += floodfill(x+1, y  )
    if y < H-1: size += floodfill(x,   y+1)
    return size

sizes = []
for y in range(H):
    for x in range(W):
        if map[y][x] < 9 and not done[y][x]:
            sizes.append(floodfill(x,y))

sizes.sort(reverse=True)
print(np.prod(sizes[0:3]))
