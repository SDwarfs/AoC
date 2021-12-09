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

# create a "done" map of the same size of type boolean, intialized with False
# to mark any map positions that have already been processed.
done = np.full((H,W), False, dtype=bool)

# recursive flood fill algorithm, which takes a starting point (x,y)
# and fills any not yet "done" marked positions without crossing 9 values
# on the map. It return the size of the filled area.
def floodfill(x,y):
    # if we are at a "9" on the map or have processed
    # this position already, abort and return a size of 0
    if map[y][x] == 9 or done[y][x]: return 0
    # mark this position as done
    # and start with a size 1 (this position)
    done[y][x] = True
    size = 1
    # recursively go left/right/up/down, and if not out of bounds,
    # add the returned size to the filled area size to be returned.
    if x > 0:   size += floodfill(x-1, y  )
    if y > 0:   size += floodfill(x,   y-1)
    if x < W-1: size += floodfill(x+1, y  )
    if y < H-1: size += floodfill(x,   y+1)
    return size

# initialize list to store the sizes
sizes = []

# go through all map positions (lines first, better caching)
for y in range(H):
    for x in range(W):
        # check if map position is not "9" or already done
        # else we end up with lots of 0 sizes in the array
        if map[y][x] == 9 or done[y][x]:
            # we found an unprocessed position that is not "9"
            # and hence part of a basin. Floodfill it and add
            # the returned size to the list.
            sizes.append(floodfill(x,y))

# sort estimated basin sizes in reversed order (largest values first)
sizes.sort(reverse=True)
# output product of the first 3 values of the list
print(np.prod(sizes[0:3]))
