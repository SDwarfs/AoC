import numpy as np

filename = "i"
regions = []

def rcopy(r):
    result = []
    for i in range(3):
        result.append([r[i][0], r[i][1]])
    return result


def getsplits(r, axis, sections):
    split1, split2 = sections
    splits = []
    # no overlap...
    if r[axis][1] < split1 or split2 < r[axis][0]:
        splits.append(rcopy(r))
        return splits
    # region totally within | [####] |
    if r[axis][0] >= split1 and r[axis][1] <= split2:
        splits.append(rcopy(r))
        return splits
    # region left overlap: | [###|###]
    if split1 <= r[axis][0] and split2 >= r[axis][0] and split2 <= r[axis][1]:
        split = rcopy(r)
        split[axis][1] = split2
        splits.append(split)

        split = rcopy(r)
        split[axis][0] = split2+1
        if (split[axis][0] <= split[axis][1]):
            splits.append(split)
        return splits
    # region right overlap:  [###|###] |
    if split1 >= r[axis][0] and split2 >= r[axis][1]:
        split = rcopy(r)
        split[axis][1] = split1-1
        if (split[axis][0] <= split[axis][1]):
            splits.append(split)

        split = rcopy(r)
        split[axis][0] = split1
        if (split[axis][0] <= split[axis][1]):
            splits.append(split)
        return splits
    # region double split    [#|###|#]
    if r[axis][0] <= split1 and r[axis][1] >= split2:
        split = rcopy(r)
        split[axis][1] = split1 - 1
        if (split[axis][0] <= split[axis][1]):
            splits.append(split)
        split = rcopy(r)
        split[axis][0] = split1
        split[axis][1] = split2
        if (split[axis][0] <= split[axis][1]):
            splits.append(split)
        split = rcopy(r)
        split[axis][0] = split2 + 1
        if (split[axis][0] <= split[axis][1]):
            splits.append(split)
        return splits


def overlap(r1, r2):
    # regions must overlap on ALL axis
    for axis in range(3):
        axis_overlap = (
          ((r1[axis][0] >= r2[axis][0]) and (r1[axis][0] <= r2[axis][1])) or
          ((r1[axis][1] >= r2[axis][0]) and (r1[axis][1] <= r2[axis][1])) or
          ((r2[axis][0] >= r1[axis][0]) and (r2[axis][0] <= r1[axis][1])) or
          ((r2[axis][1] >= r1[axis][0]) and (r2[axis][1] <= r1[axis][1]))
        )
        if not axis_overlap: return False
    return True


def addRegion(r, val):
    global regions
    regions_new = []
    for r2 in regions:
        if not overlap(r2,r):
            regions_new.append(r2)
            continue
        # split region...
        xsplits = getsplits(r2, 0, r[0])

        ysplits = []
        for i in range(len(xsplits)):
            ysplits += getsplits(xsplits[i], 1, r[1])

        zsplits = []
        for i in range(len(ysplits)):
            zsplits += getsplits(ysplits[i], 2, r[2])

        for i in range(len(zsplits)):
            if not overlap(zsplits[i], r):
                regions_new.append(zsplits[i])

    if val == 1:
        regions_new.append(r)
    regions = regions_new


def getSum():
    sum = 0
    for r in regions:
        size = 1
        for axis in range(0,3):
            size *= (r[axis][1]-r[axis][0]+1)
        sum += size
    return sum

for line in open(filename):
    line = line.rstrip()
    val, coords = line.split(" ")
    coords = coords.split(",")
    x1, x2 = coords[0].split("..")
    y1, y2 = coords[1].split("..")
    z1, z2 = coords[2].split("..")
    _, x1 = x1.split("=")
    _, y1 = y1.split("=")
    _, z1 = z1.split("=")
    if val == "on": val = 1
    else: val = 0
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)
    addRegion([[x1,x2],[y1,y2],[z1,z2]],val)

print(getSum())
