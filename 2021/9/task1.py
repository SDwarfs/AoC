lines = [x.rstrip() for x in open("input.txt")]
map = []
for line in lines:
    if line != "": map.append([int(x) for x in line])
H = len(map)
W = len(map[0])
count = 0
for y in range(H):
    for x in range(W):
        cur = map[y][x]
        if x > 0   and map[y][x-1]<=cur: continue
        if x < W-1 and map[y][x+1]<=cur: continue
        if y > 0   and map[y-1][x]<=cur: continue
        if y < H-1 and map[y+1][x]<=cur: continue
        count += 1 + int(cur)
print(count)
