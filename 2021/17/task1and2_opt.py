import re
line = open("i").readline().strip()
m = re.findall(r"target area: x=([-0-9]+)..([-0-9]+), y=([-0-9]+)..([-0-9]+)", line)
x1, x2, y1, y2 = [int(x) for x in m[0]]

# The max vertical speed is always -y1 - 1 as the velocity
# goes like n, n-1, ..., 1, 0, -1, -2, ..., -n, .. and reaching
# velocity -n the sum of the velocity values is zero, hence the probe
# is again at y = 0, the next velocity will be -1 the negative start speed
# hence the starting velocity speed must be 1 lower than the negated minimum
# value of the target area, or it will shoot over it in the next step:
maxvy = -y1 - 1
# the maximum height will then be the sum of all speed values until the
# vertical speed reaches 0. This is the sum of all numbers maxvx downto 0
# or just 1 to maxvx, which can be calculated with the Gauss Formula:
# N * (N+1) / 2, we use // 2 to get the result as an integer value
maxheight = maxvy * (maxvy+1)//2
# And done:
print("Part 1:", maxheight)

# For part 2 we need a function that checks if the shot with a given x/x speed
# (given as vx, vy) lands in the area (returns 1) or overshoots (returns 0):
def doesHit(vx,vy):
    global x1, x2, y1, y2 # target area
    x = y = 0             # start position
    while x <= x2 and y >= y1: # as long we did not overshoot
        # move probe forward by vx, vy
        x += vx
        y += vy
        # now adapt vx / vy according rules for drag and gravity
        # note that vx < 0 does not make sense, so we skip it here
        if vx > 0: vx -= 1
        vy -= 1
        # check, if we land inside the target area: if so, return 1
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return 1
    # return 0 when aborting, due to overshooting
    return 0

# count the number of valid hits
count = 0
# go through all vy values:
# for vy from y1 to -y1-1 (below y1 will not hit, over -y1-1 will overshoot)
# for vx from 1 to x2 (needs to be over 0 and >x2 will overshoot in 1st step)
# count all the hits and ouput the value:
for vy in range(y1, -y1):
    for vx in range(1, x2+1):
        count += doesHit(vx, vy)
print("Part 2:", count)
