# config: num cycles to execute
num_cycles = 10
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


def apply(polymer):
    # init new polymer string
    new_polymer = ""
    # go through the old polymer string
    for i in range(len(polymer)-1):
        # append first character of the current pair
        new_polymer += polymer[i]
        # get the current pattern (current + next character)
        pattern = polymer[i:i+2]
        # if pattern is in rule set, append (or indirectly insert)
        # the new character from that rule
        if pattern in rules:
            new_polymer += rules[pattern]
    # append the last polymer character, which doesn't have a next
    # character to form a pair
    new_polymer += polymer[len(polymer)-1]
    # return result
    return new_polymer

# apply the insertion rule <num_cycles> times
for i in range(num_cycles):
    polymer = apply(polymer)

# go through all polymer characters and sum up the count of them
counts = {}
for char in polymer:
    counts[char] = counts.get(char, 0) + 1

# get max() and min() of the count values
# and calculate/print the result max()-min()
result = max(counts.values()) - min (counts.values())
print(result)
