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

# total_risk_level initialized to 0
total_risk_level = 0

# go through all lines first (=faster because of CPU cache hits/misses)
for y in range(H):
    # go thourh all x positions in the line
    for x in range(W):
        # estimate current positions value
        val = map[y][x]
        # check if any horizontal/vertical neighbor exists that has
        # a lower value, if so: skip the rest of the x-loop code
        if x > 0   and map[y][x-1] <= val: continue
        if x < W-1 and map[y][x+1] <= val: continue
        if y > 0   and map[y-1][x] <= val: continue
        if y < H-1 and map[y+1][x] <= val: continue
        # since there are no such neighbors, we found a local minimum
        # and can add the risk level (1 + val) to the sum.
        total_risk_level += 1 + val
print(total_risk_level)
