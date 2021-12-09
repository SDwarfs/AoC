import numpy as np

lines = [x.rstrip() for x in open("input.txt")]
input = [int(x) for x in lines[0].split(",")]
print(input)

for i in range(256):
    numnew = 0
    for x in range(len(input)):
        if input[x] == 0:
            input[x] = 6
            numnew += 1
        else:
            input[x] -= 1
    for x in range(numnew):
        input.append(8)
print(len(input))
