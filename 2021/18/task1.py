import json
import numpy as np

numbers = []
lines = []
for line in open("i"):
    line = line.rstrip()
    if line != "":
        numbers.append(json.loads(line))
        lines.append(line)


def set(num, path, value):
    ptr = num
    for i in range(len(path)-1):
        ptr = ptr[path[i]]
    if isinstance(value, int):
        ptr[path[-1]] = value
    else:
        ptr[path[-1]] = []
        ptr[path[-1]].append(value[0])
        ptr[path[-1]].append(value[1])


def get(num, path):
    ptr = num
    for i in range(len(path)-1):
        ptr = ptr[path[i]]
    return ptr[path[-1]]


def add(num, path, value):
    new_value = get(num, path) + value
    set(num, path, new_value)

def isPair(num, path):
    if len(path) == 0:
        return True
    ptr = num
    for i in range(len(path)-1):
        ptr = ptr[path[i]]
    return not isinstance(ptr[path[-1]], int)

def addRight(num, path, value):
    for i in reversed(range(len(path))):
        if path[i] == 0:
            path2 = path[0:i]
            path2.append(1)
            while isPair(num, path2):
                path2.append(0)
            add(num, path2, value)
            return


def addLeft(num, path, value):
    for i in reversed(range(len(path))):
        if path[i] == 1:
            path2 = path[0:i]
            path2.append(0)
            while isPair(num, path2):
                path2.append(1)
            add(num, path2, value)
            return

def explode(num, path = []):
    if not isPair(num, path):
        return False
    if len(path) == 4:
        addLeft(num, path, get(num, path)[0])
        addRight(num, path, get(num, path)[1])
        set(num, path, 0)
        return False
    else:
        pathL = path.copy()
        pathL.append(0)
        result = explode(num, pathL)
        if result == True: return result

        pathR = path.copy()
        pathR.append(1)
        result = explode(num, pathR)
        if result == True: return result
        return False

def split(num, path=[]):
    pathL = path.copy()
    pathL.append(0)
    pathR = path.copy()
    pathR.append(1)
    if isPair(num, pathL):
        result = split(num, pathL)
        if result == True: return result
    else:
        val = get(num, pathL)
        if val >= 10:
            set(num, pathL, [val//2, val - val//2])
            return True
    if isPair(num, pathR):
        result = split(num, pathR)
        if result == True: return result
    else:
        val = get(num, pathR)
        if val >= 10:
            set(num, pathR, [val//2, val - val//2])
            return True
    return False


def reduce(num):
    while True:
        result = explode(num)
        if result == True: continue
        result = split(num)
        if result == True: continue
        return


def magnitude(num, path=[]):
    if isPair(num, path):
        pathL = path.copy()
        pathL.append(0)
        pathR = path.copy()
        pathR.append(1)
        return 3*magnitude(num, pathL) + 2*magnitude(num, pathR)
    else:
        return get(num,path)

num = json.loads(lines[0])
for i in range(1, len(numbers)):
    num = [num, json.loads(lines[i])]
    reduce(num)
print("PART 1:", magnitude(num))

bestmag = -1
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j: continue
        num = [json.loads(lines[i]),json.loads(lines[j])]
        reduce(num)
        mag = magnitude(num)
        if mag > bestmag: bestmag = mag
print("PART 2: ", bestmag)
