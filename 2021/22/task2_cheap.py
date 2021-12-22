from numba import njit
import numpy as np
import re

# parse input file into quads[] in the format [x1,x2,y1,y2,z1,z2,value],
# where value=1 for "on" and 0 for "off"
quads = []
for line in open("i"):
    m = re.search(r"([a-z]+) x=([\-0-9]+)..([\-0-9]+),y=([\-0-9]+)..([\-0-9]+),z=([\-0-9]+)..([\-0-9]+)", line.rstrip())
    quad = [int(m.group(i+2)) for i in range(6)]
    quad.append(1 if m.group(1) == "on" else 0)
    quads.append(quad)

# Go through all quads and estimate at which x, y and z coordinates
# we split the total 3d-cube in parts
coords = [[],[],[]]
for quad in quads:
    for axis in range(3):
        # append any left coordinate normal
        coords[axis].append(quad[2*axis+0])
        # but append the right coordinate + 1
        # as the this will be the left coordinates
        # of the neightbor next to it...
        coords[axis].append(quad[2*axis+1] + 1)
# make the coords unique and sort them...
for axis in range(3):
    coords[axis] = list(set(coords[axis]))
    coords[axis].sort()

# Calculate the needed dimensions of the map in X/Y/Z
[X, Y, Z] = [len(coords[axis]) for axis in range(3)]
# ...and create a map initialized with 0
map = np.zeros((X,Y,Z), 'uint8')
# this will be a temporary array to hold the coordinate ranges
# mapped to map indices in the following loop
map_coords = np.zeros((6), 'int')
# go through all quads again...
for quad in quads:
    # map the coordinates to map indices...
    for axis in range(3):
        # we just lookup the index of the coordinates in the
        # coordinates list for the according axis
        map_coords[axis*2+0] = coords[axis].index(quad[axis*2+0])
        # note that we calculate the right index as "+1"
        # so we can directly use it for the [from:to] ranges
        # where to is "+1" used by python / numpy
        map_coords[axis*2+1] = coords[axis].index(quad[axis*2+1]+1)
    # now just set the map region to the value (quad[6]) of that quad.
    map[map_coords[0]:map_coords[1], map_coords[2]:map_coords[3], map_coords[4]:map_coords[5] ] = quad[6]

# getSum() calculates the size of volume of cubes set to 1
# going through the whole array is quite slow to do directly with interpreted
# code, hence we use a jit compiled method for this...
@njit
def getSum(X,Y,Z, map, CX, CY, CZ):
    sum = 0
    # We go through all coordinates of each axis, except the last ones
    # which can only be the right border of a region
    for x in range(X-1):
        # for each dimension we calculate the size of that mapped area
        # in that dimension (= coordinate difference to next coordinate)
        xsize = CX[x+1] - CX[x]
        # same for y axis...
        for y in range(Y-1):
            ysize = CY[y+1] - CY[y]
            # and now for z axis...
            for z in range(Z-1):
                zsize = CZ[z+1] - CZ[z]
                # now we multiply the map value for that region (0 or 1)
                # by the size of that region (which is the size of the
                # region in case the map value is 1, else 0) to the total sum
                sum += int(map[x,y,z]) * xsize * ysize * zsize
    # and done... return sum
    return sum

# to call the @njit compiled code, we need to convert those coords lists
# to np.arrays() which the jit compiler can handle. Also no access to
# global variables can be used, so we need to hand in everything via params
sum = getSum(X,Y,Z, map, np.array(coords[0]), np.array(coords[1]), np.array(coords[2]))

# finally, we can output the result...
print(sum)
