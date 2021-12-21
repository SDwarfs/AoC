import numpy as np
import timeit

filename = "i"

part = 1
image = []
IEA = []
for line in open(filename):
    line = line.rstrip()
    line = [(0 if c=='.' else 1) for c in line]
    if len(line)==0:
        part += 1
        continue
    if part == 1:
        IEA += line
        continue
    if part == 2:
        image.append(line)

#print(IEA)
#print(image)

H=len(image)
W=len(image[0])
iimg = {}
for y in range(H):
    iimg[y] = {}
    for x in range(W):
        if image[y][x] == 1:
            iimg[y][x] = 1


def getRange(iimg):
    miny = min(iimg.keys())
    maxy = max(iimg.keys())
    minx = maxx = 0
    for y in range(miny,maxy+1):
        if not y in iimg: continue
        minx = min(minx, min(iimg[y].keys()))
        maxx = max(maxx, max(iimg[y].keys()))
    return (minx,maxx,miny,maxy)


def enhance(iimg, fill):
    new_fill = IEA[fill*511]
    new_not_fill = (new_fill + 1) % 2
    new_iimg = {}
    minx, maxx, miny, maxy = getRange(iimg)
    for y in range(miny-1,maxy+2):
        for x in range(minx-1,maxx+2):
            idx = 0
            for ry in range(y-1,y+2):
                for rx in range(x-1,x+2):
                    idx *= 2
                    if not ry in iimg:
                        idx += fill
                    elif not rx in iimg[ry]:
                        idx += fill
                    else:
                        idx += iimg[ry][rx]
            if IEA[idx] != new_fill:
                if not y in new_iimg: new_iimg[y] = {}
                new_iimg[y][x] = new_not_fill
    return new_iimg, new_fill

def print_img(iimg, fill):
    minx, maxx, miny, maxy = getRange(iimg)
    for y in range(miny,maxy+1):
        for x in range(minx, maxx+1):
            if y in iimg and x in iimg[y]:
                print("#", end='')
            else:
                print(".", end='')
        print("")
    print("")

def getLit(iimg, fill):
    if fill == 1: return -1
    sum = 0
    for y in iimg.keys():
        sum += len(iimg[y].keys())
    return sum

start = timeit.default_timer()
fill = 0
#print_img(iimg, fill)
for i in range(50):
    iimg, fill = enhance(iimg, fill)
    #print_img(iimg, fill)
    if i == 1: print("PART 1:", getLit(iimg, fill))
print("PART 2:", getLit(iimg, fill))
stop = timeit.default_timer()
print("Time: ", stop-start)
