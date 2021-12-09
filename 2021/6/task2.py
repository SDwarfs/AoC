import numpy as np

lines = [x.rstrip() for x in open("input.txt")]
input = [int(x) for x in lines[0].split(",")]
print(input)
count = np.zeros((9), 'uint64')
for x in input:
    count[x] += 1

for i in range(256):
    numnew = count[0]
    count[0:8] = count[1:9]
    count[8] = numnew
    count[6] += numnew
print(sum(count))
