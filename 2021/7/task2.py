import numpy as np

lines = [x.rstrip() for x in open("input.txt")]
input = [int(x) for x in lines[0].split(",")]
#print(input)
# exit()


ramp = np.zeros((max(input)+1), 'int64')
ramp2 = np.zeros((max(input)+1), 'int64')
ramp2[0] = 0
for i in range(1,max(input)+1):
    ramp[i] = ramp[i-1] + 1
    ramp2[i] = sum(ramp[0:i+1])

print(ramp)
print(ramp2)

besti = 0
bestfuel = 1E10
for i in range(min(input),max(input)+1):
    fuel = 0
    for x in input:
        dist = abs(x-1)
        cost = ramp2[dist]
        fuel += ramp2[abs(x-i)]
    if fuel<bestfuel:
        print(i, fuel)
        bestfuel = fuel
        besti = i
print(besti,bestfuel)
