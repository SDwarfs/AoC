depth = hpos = 0
NUMBITS=12
lines = 0
sum = [0 for i in range(NUMBITS)]
for line in open("input.txt"):
    lines+=1
    for i in range(NUMBITS):
        sum[i] += int(line[i])
half = lines/2
gamma = epsilon = 0
for i in range(NUMBITS):
    val = pow(2, NUMBITS-i-1)
    if sum[i]>half:
        gamma += val
    else:
        epsilon += val
print(gamma, epsilon, gamma*epsilon)
