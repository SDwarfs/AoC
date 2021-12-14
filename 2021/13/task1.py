import numpy as np

# read all input lines into lines[] and strip off trailing whitespaces
lines = [x.rstrip() for x in open("input.txt")]

def printIt(pts):
    mx = max(pts[:,0])
    my = max(pts[:,1])
    #print(pts[:,0])
    #print(pts[:,1])
    #print("MAX: ", mx, my)
    map = np.zeros((my+1,mx+1), 'uint8')
    for p in points:
        map[p[1]][p[0]] = 1
    sum = 0
    for y in range(my+1):
        for x in range(mx+1):
            if map[y][x] == 1:
                #print('#', end='')
                sum += 1
            else:
                pass
                #print('.', end='')
        #print("")
    return sum


points = []
section = 1
for line in lines:
    if line == "":
        section = 2
        N = len(points)
        points = np.array(points)
        continue
    if section == 1:
        (x,y) = line.split(",")
        x = int(x)
        y = int(y)
        points.append((x,y))
    else:
        printIt(points)
        (a,b,how) = line.split(" ")
        (axis,coord) = how.split("=")
        coord = int(coord)
        if axis == "x": axis = 0
        else: axis = 1
        print("along", axis, coord)
        print(N)
        for i in range(N):
            if points[i][axis] > coord:
                points[i][axis] = 2*coord - points[i][axis]
        break
sum = printIt(points)
print("RESULT: ",sum)
