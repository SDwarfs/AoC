# config: num cycles to execute
num_cycles = 40
# input file name
fn = "input.txt"

###
# parse the input file into variable "polymer" (string) and "rules" (Dict)
# which maps the patterns to the character to be inserted.
###
section = 1
rules = {}
# go through all lines in file
for line in open(fn):
    # strip any whilespaces at the end (right side)
    line = line.rstrip()
    if line == "":     section = 2    # if there is empty line, section 2 starts
    elif section == 1: polymer = line # if section == 1, we save it as polymer string
    else:
        # section 2: PAIR-PATTERN => INSERT CHARACTER
        (rulea, ruleb) = line.split(' -> ')
        rules[rulea] = ruleb

# convert polymer string into dict of pairs with counts
pairs = {}
for i in range(len(polymer)-1):
    pair = polymer[i:i+2]
    pairs[pair] = pairs.get(pair, 0) + 1

# function applys the replacement rules to a polymer pair list once
def apply(pairs):
    # create a new pair count dictionary, since in-place modifications
    # of the original dict will lead to undesired behaviour
    new_pairs = {}
    # go through all pair entries:
    for pair, count in pairs.items():
        if pair in rules:
            # if matching rule exists generate new pairs ...
            char = rules[pair]
            new_pair_1 = pair[0] + char # by appending
            new_pair_2 = char + pair[1] # or prepending the insertion character
            # and finally add their new occourances to the new_pairs dictionary
            new_pairs[new_pair_1] = new_pairs.get(new_pair_1, 0) + count
            new_pairs[new_pair_2] = new_pairs.get(new_pair_2, 0) + count
        else:
            # if no rule exists, just add occourances to new_pairs dictionary
            new_pairs[pair] = new_pairs.get(pair, 0) + count
    # return the new pairs dictionary
    return new_pairs

# run <num_cycles> cycles and apply() the rules
for i in range(num_cycles):
    pairs = apply(pairs)

# now count the characters
# note: that we need to add the last character of the polymer
# which will always stay the last one in the resultm since we only
# sum the first character of the pairs.
# Hence, we initialize "counts" with 1 for that last polymer character.
last_c = polymer[len(polymer)-1]
counts = { last_c: 1 }
# then we go through all pairs and add the counts of each first character
# to the character count list
for pair, count in pairs.items():
    firstchar = pair[0]
    counts[firstchar] = counts.get(firstchar, 0) + count

# estimate the minimum and the maximum counts
# and calculate/output max - min as the result.
result = max(counts.values()) - min(counts.values())
print(result)
