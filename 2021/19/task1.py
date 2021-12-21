filename = "i"

def roll(v):
    return (v[0], v[2], -v[1])

def turn_cw(v):
    return (v[1],-v[0],v[2])

def turn_ccw(v):
    return (-v[1],v[0],v[2])

def sequence(m):
  n = 0
  n += 1
  yield(m)
  for r in range(6):
    m = roll(m)
    n += 1
    yield(m)

    if r % 2 == 0:
        for t in range(3):
            m = turn_cw(m)
            n += 1
            yield(m)
            if n >= 24: return
    else:
        for t in range(3):
            m = turn_ccw(m)
            n += 1
            yield(m)
            if n >= 24: return

scanners = []
scan = []
for i in range(24): scan.append([])
for line in open(filename):
    line = line.rstrip()
    if line == "":
        if len(scan)>0:
            scanners.append(scan)
        scan = []
        for i in range(24): scan.append([])
        continue
    if line[0:3] == "---":
        continue
    v = [int(x) for x in line.split(",")]
    r = 0
    for rv in sequence(v):
        scan[r].append(rv)
        r += 1
if len(scan)>0:
    scanners.append(scan)

def isInRange(v):
    if abs(v[0]) > 1000: return False
    if abs(v[1]) > 1000: return False
    if abs(v[2]) > 1000: return False
    return True

def equals(v,u):
    return v[0]==u[0] and v[1]==u[1] and v[2]==u[2]


# scanner a must see all beacons inside the range of -1000 .. 1000
# of any direction...
def seesAllBeaconsInRange(a, b):
    overlapCount = 0
    for u in b:
        # skip any beacons that would not be in range
        if not isInRange(u): continue
        overlapCount += 1
        # all the others must be found:
        found = False
        for v in a:
            if equals(u,v):
                found = True
                break
        if not found:
            return 0
    return overlapCount >= 3


def doesMatch(a,b,delta):
    # scanner a sees scanner b's results as b + delta
    b2 = []
    for i in range(len(b)):
        b2.append([b[i][dim] + delta[dim] for dim in range(3)])
    # b2 = [b[i][dim] + delta[dim] for dim in range(3) for i in range(len(b))]
    if not seesAllBeaconsInRange(a, b2):
        return False
    # scanner b sees  scanner a's results as a - delta
    a2 = []
    for i in range(len(a)):
        a2.append([a[i][dim] - delta[dim] for dim in range(3)])
    if not seesAllBeaconsInRange(b, a2):
        return False
    return True


def getBestMatch(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            delta = [a[i][dim] - b[j][dim] for dim in range(3)]
            if doesMatch(a,b,delta):
                return delta
    return None

N = len(scanners)
print("SCANNERS:", N)

global_deltas = {
    0: [0,0,0]
}
global_rotations = {
    0: 0
}
found = [ 0 ]
unmatched = [x for x in range(1, N)]

while len(unmatched) > 0:
    i = found.pop(0)
    ri = global_rotations[i]
    toberemoved = []
    for j in unmatched:
        for rj in range(24):
            #print("i:",i,"j:", j,"ri:", ri, "rj:",rj)
            delta = getBestMatch(scanners[i][ri], scanners[j][rj])
            if delta is None: continue
            found.append(j)
            toberemoved.append(j)
            global_deltas[j] = [global_deltas[i][dim] + delta[dim] for dim in range(3)]
            global_rotations[j] = rj
            print(i, j, rj, delta, global_deltas[j])
            break
    for j in toberemoved:
        unmatched.remove(j)

beacons = {}
for i in range(N):
    delta = global_deltas[i]
    ri = global_rotations[i]
    for v in scanners[i][ri]:
        u = [v[dim] + delta[dim] for dim in range(3)]
        id = str(u[0])+","+str(u[1])+","+str(u[2])
        beacons[id] = u

print(len(beacons.items()))

maxdist = 0
for i in range(N-1):
    for j in range(i,N):
        dist = sum([abs(global_deltas[i][dim] - global_deltas[j][dim]) for dim in range(3)])
        maxdist = max(maxdist, dist)
print(maxdist)

#print(N)
#print(scanners[N-1])
