if False:
    NUMBITS = 5
    fn = "sample.txt"
else:
    NUMBITS=12
    fn = "input.txt"

lines = []
for line in open(fn):
    lines.append(line.strip())

def getMost(list, bit):
    N = len(list)
    count = 0
    for i in range(N):
        if list[i][bit] == "1":
            count += 1
    if count >= N/2:
        return 1
    else:
        return 0

def getLeast(list, bit):
    return getMost(list, bit) ^ 1


def filter(list, type):
    for bit in range(NUMBITS):
        if (len(list) == 1):
            return list[0]
        filtered = []
        if type == 0:
            want = getMost(list, bit)
        else:
            want = getLeast(list, bit)
        for i in range(len(list)):
            if int(list[i][bit]) == want:
                filtered.append(list[i])
        list = filtered
    return list[0]

def getVal(s):
    val = 0
    for i in range(NUMBITS):
        if s[i] == "1":
            val += pow(2, NUMBITS-1-i)
    return val

oxy=filter(lines, 0)
print("OXY: ", oxy, getVal(oxy))

co2=filter(lines, 1)
print("CO2: ", co2, getVal(co2))

print("MULT: ", getVal(oxy)*getVal(co2))
