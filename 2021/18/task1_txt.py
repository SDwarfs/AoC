numbers = []
for line in open("i"):
    line = line.rstrip()
    if line != "":
        numbers.append(line)


def add(s, start, end, step, value):
    for i in range(start, end, step):
        if s[i] >= '0' and s[i] <= '9':
            for j in range(i+step, end, step):
                if s[j] >= '0' and s[j] <= '9': continue
                j -= step
                value += int(s[min(i,j):max(i,j)+1])
                return s[0:min(i,j)]+str(value)+s[max(i,j)+1:]
    return s

def explode(s):
    depth = 0
    for i in range(len(s)):
        if s[i] == '[':
            depth += 1
            if (depth == 5):
                num = 0
                for j in range(i+1, len(s)):
                    if s[j] >= '0' and s[j] <= '9':
                        num *= 10
                        num += int(s[j])
                    if s[j] == ',':
                        left = num
                        num = 0
                    elif s[j] == ']':
                        right = num
                        return add(s[0:i], i-1, -1, -1, left) + "0" + add(s[j+1:], 0, len(s)-j-1, 1, right)
        if s[i] == ']':
            depth -= 1
    return s

def split(s):
    start = -1
    num = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            if start == -1: start = i
            num *= 10
            num += int(s[i])
        else:
            if num > 9:
                return s[0:start]+"["+str(num//2)+","+str(num - num//2)+"]"+s[i:]
            num = 0
            start = -1
    return s


def magnitude(s):
    side = [0] * 4
    sum = [0] * 4
    depth = 0
    num = 0
    for i in range(len(s)):
        if s[i] == '[':
            depth += 1
            side[depth-1] = 0
            sum[depth-1] = 0
            num = 0
        elif s[i] == ']':
            sum[depth-1] += num * 2
            depth -= 1
            if side[depth-1] == 0:
                sum[depth-1] += sum[depth] * 3
            else:
                sum[depth-1] += sum[depth] * 2
            num = 0
        elif s[i] == ',':
            sum[depth-1] += num * 3
            side[depth-1] = 1
            num = 0
        elif s[i] >= '0' and s[i] <= '9':
            num *= 10
            num += int(s[i])
    return sum[0]


def addNum(n1, n2):
    num = "["+str(n1)+","+str(n2)+"]"
    while True:
        result = explode(num)
        if result != num:
            num = result
            continue
        result = split(num)
        if result != num:
            num = result
            continue
        break
    return num


num = numbers[0]
for i in range(1,len(numbers)):
    num = addNum(num, numbers[i])
print("PART 1:", magnitude(num))

bestmag = -1
N = len(numbers)
for i in range(N):
    for j in range(N):
        if (i != j):
            mag = magnitude(addNum(numbers[i],numbers[j]))
            bestmag = max(mag, bestmag)
print("PART 2:", bestmag)
