import numpy as np

lines = [x.rstrip() for x in open("input.txt")]
input = [int(x) for x in lines[0].split(",")]
#print(input)
# exit()
besti = 0
bestfuel = 1E10
for i in range(min(input),max(input)+1):
    fuel = 0
    for x in input:
        fuel += abs(x-i)
    if fuel<bestfuel:
        print(i, fuel)
        bestfuel = fuel
        besti = i
print(besti,bestfuel)
