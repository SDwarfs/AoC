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


def apply(pairs):
    new_pairs = {}
    #print(pairs)
    for k,v in pairs.items():
        #print("KV: ", k,v)
        if k in rules:
            c = rules[k]
            p1 = k[0] + c
            p2 = c + k[1]
            if not p1 in new_pairs: new_pairs[p1] = 0
            new_pairs[p1] += v
            if not p2 in new_pairs: new_pairs[p2] = 0
            new_pairs[p2] += v
        else:
            if not k in new_pairs: new_pairs[k] = 0
            new_pairs[k] += v
    return new_pairs

pairs = {}
for i in range(len(polymer)-1):
    pair = polymer[i:i+2]
    if not pair in pairs: pairs[pair] = 0
    pairs[pair] += 1


#print(polymer)
for i in range(40):
    pairs = apply(pairs)
    #print(polymer)

last_c = polymer[len(polymer)-1]
counts = { last_c: 1 }
for k,v in pairs.items():
    c = k[0]
    if not c in counts: counts[c] = 0
    counts[c] += v

l=[v for k,v in sorted(counts.items(), key=lambda c:c[1])]
print(l[len(l)-1] - l[0])
print(sum(l))
