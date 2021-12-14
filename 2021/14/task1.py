import numpy as np

lines = [x.rstrip() for x in open("input.txt")]

section = 1
rules = {}
polymer = ""
for line in lines:
    if line == "":
        section = 2
        continue
    if section == 1:
        polymer = line
    else:
        (rulea, ruleb) = line.split(' -> ')
        rules[rulea] = ruleb




def apply(polymer):
    new_polymer = ""
    for i in range(len(polymer)-1):
        new_polymer += polymer[i]
        pattern = polymer[i:i+2]
        #print("PATTERN:", pattern)
        if pattern in rules:
            new_polymer += rules[pattern]
    new_polymer += polymer[len(polymer)-1]
    return new_polymer

#print(polymer)
for i in range(40):
    polymer = apply(polymer)
    #print(polymer)

counts = {}
for x in polymer:
    if not x in counts: counts[x] = 0
    counts[x] += 1

l=[v for k,v in sorted(counts.items(), key=lambda c:c[1])]
print(l[len(l)-1] - l[0])
