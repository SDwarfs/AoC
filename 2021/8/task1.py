import numpy as np

def toArr(s):
    bits = np.zeros((7), 'uint8')
    for c in s:
        bits[ord(c) - ord('a')] = 1
    return bits

def findNOn(d, n):
    f = []
    for x in d:
        if sum(x) == n:
            f.append(x)
    return f

def find1NOn(d, n):
    return findNOn(d,n)[0]

def findDiff(a,b):
    l = []
    for i in range(7):
        if a[i] != b[i]:
            l.append(i)
    return l

def find1Diff(a,b):
    return findDiff(a,b)[0]

def getCounts(d):
    c = []
    for seg in range(7):
        sum = 0
        for i in range(10):
            sum += d[i][seg]
        c.append(sum)
    return c

def notIn(p, x):
    for i in range(7):
        if i != x and p[i] == 1:
            return i
    return -1

def getIndex(l, x):
    f = []
    for i in range(len(l)):
        if l[i] == x:
            f.append(i)
    return f

def get1Index(l, x):
    return getIndex(l, x)[0]


def decodeSeg(code, a, b, c, d, e, f, g):
    if code[a] == 1:
        # 0, 2, 3, 5, 6, 7, 8, 9
        if code[b] == 1:
            # 0, 5, 6, 8, 9
            if code[c] == 1:
                # 0, 8, 9
                if code[d] == 1:
                    # 8, 9
                    if code[e] == 1:
                        return 8
                    else:
                        return 9
                else:
                    return 0
            else:
                # 5, 6
                if code[e] == 1:
                    return 6
                else:
                    return 5
        else:
            # 2, 3, 7
            if code[g] == 1:
                # 2, 3
                if code[e] == 1:
                    return 2
                else:
                    return 3
            else:
                return 7
    else:
        # 1, 4
        if code[d] == 1:
            return 4
        else:
            return 1
        pass

counter = 0

def parseLine(line):
    global counter
    parts = line.split(" | ")
    # print(line)
    digits = parts[0]
    codes = parts[1]
    digits_num = [toArr(x) for x in digits.split(" ")]
    codes_num = [toArr(x) for x in codes.split(" ")]
    counts = getCounts(digits_num)
    # for x in codes_num:
    #     s = sum(x)
    #     if s == 2 or s == 4 or s == 3 or s == 7: counter = counter + 1
    #     print(x, s, counter)
    # return
    # print(counts)
    # find segments by unique appearance counts
    e = get1Index(counts, 4)
    b = get1Index(counts, 6)
    f = get1Index(counts, 9)
    p1 = find1NOn(digits_num, 2) # find "1"
    p7 = find1NOn(digits_num, 3) # find "7"
    p4 = find1NOn(digits_num, 4) # find "4"
    a = find1Diff(p1, p7) # difference => a
    c = notIn(p1, f)      # other segment than "f" in digit "1"
    occ7 = getIndex(counts, 7) # [d,g] or [g,d]
    occ8 = getIndex(counts, 8) # [a,c] or [c,a]
    # switch of b, c, f => result: only d
    p4[b] = 0
    p4[c] = 0
    p4[f] = 0
    for i in range(7):
        if p4[i] == 1:
            d = i
            break
    print("D: ", d, p4)
    if occ7[0] == d:
        g = occ7[1]
    else:
        g = occ7[0]

    val = 0
    for code in codes_num:
        digit = decodeSeg(code, a, b, c, d, e, f, g)
        val *= 10
        val += digit
        # if digit == 1: counter = counter + 1
        # if digit == 4: counter = counter + 1
        # if digit == 7: counter = counter + 1
        # if digit == 8: counter = counter + 1
        print("DECODE: ", code, digit, counter)
    counter += val
    print("")
    # exit()
    # print(digits,codes)
    # exit()
lines = [parseLine(x.rstrip()) for x in open("input.txt")]

print(counter)
