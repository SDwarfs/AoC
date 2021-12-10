import numpy as np

lines = [x.rstrip() for x in open("input.txt")]

linescores = []
for line in lines:
    open = []
    corrupted = False
    for c in line:
        if c == '[':
            open.append("]")
        elif c == '(':
            open.append(")")
        elif c =='{':
            open.append("}")
        elif c == '<':
            open.append(">")
        elif c == ']' or c == ")" or c == "}" or c == '>':
            e = open[len(open)-1]
            if c != e:
                # print("corrupted", line, e, "exprected", c, "found")
                corrupted = True
                break
            open = open[:-1]
    if len(open) > 0 and not corrupted:
        N = len(open)
        linescore = 0
        for x in range(N):
            c = open[N-x-1]
            linescore *= 5
            if c == ')': linescore += 1
            if c == ']': linescore += 2
            if c == '}': linescore += 3
            if c == '>': linescore += 4
        linescores.append(linescore)
        print("incomplete", line, open, linescore)
print(linescores)
linescores.sort()
print(linescores[len(linescores)//2])
