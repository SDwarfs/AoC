import numpy as np

lines = [x.rstrip() for x in open("input.txt")]

open = []
points = 0
for line in lines:
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
                print("corrupted", line, e, "exprected", c, "found")
                if c == ')': points += 3
                if c == ']': points += 57
                if c == '}': points += 1197
                if c == '>': points += 25137
                break
            open = open[:-1]
    if len(open) > 0:
        print("incomplete")
print(points)
