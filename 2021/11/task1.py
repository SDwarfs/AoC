import numpy as np

# read all input lines into lines[] and strip off trailing whitespaces
lines = [x.rstrip() for x in open("input.txt")]

# for each line, thats not empty (i.e. last line of file)
# create a list containing all character converted to int values
# and append it to map[]
map = []
for line in lines:
    if line != "": map.append([int(x) for x in line])

# estimate size of map: H = height / number of lines, W = width of the lines
H = len(map)
W = len(map[0])


def printMap(map,r):
    return
    global W, H
    print("STEP: ", r+1)
    for y in range(H):
        for x in range(W):
            print(map[y][x], end='')
        print("")
    print("")

count = 0
for r in range(1000):
    printMap(map, r-1)

    for y in range(H):
        for x in range(W):
            map[y][x] += 1
    printMap(map, r-1)
    flashed = np.zeros((H,W), 'uint8')
    found = True
    while found:
        found = False
        for y in range(H):
            for x in range(W):
                if map[y][x] > 9: # and flashed[y][x] == 0:
                    map[y][x] = 0
                    flashed[y][x] = 1
                    found = True
                    count += 1
                    for dy in range(-1,2):
                        if (dy+y) < 0: continue
                        if (dy+y) >= H: continue
                        for dx in range(-1,2):
                            if (dx+x) < 0: continue
                            if (dx+x) >= W: continue
                            if dx == 0 and dy == 0: continue
                            if flashed[y+dy][x+dx] == 1: continue
                            map[y+dy][x+dx] += 1
    printMap(map, r)
    if np.sum(flashed) == H*W:
        print(r+1)
        exit()
#print(count)
