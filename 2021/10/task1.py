# read lines from file and strip whitespaces at the end
lines = [x.rstrip() for x in open("input.txt")]

# matching closing parenthesis
matching = { '(': ')', '[': ']', '{': '}',  '<': '>'   }
# points for synthax errors with these expected closing parenthesis
points   = { ')': 3,   ']': 57,  '}': 1197, '>': 25137 }


def lineScore(line):
    # reset the list of expected closing parenthesis
    open = []
    for c in line:
        if c in matching:
            # if its one of the opening parenthesis
            # add the matching closing one to the list
            open.append(matching[c])
        else:
            # if not it's a closing one, and needs to match the last
            # opened one... which needs to be closed first
            expected = open[-1]
            # if not expected, return score for this faulty character
            if c != expected: return points[c]
            # else: remove correctly closed parenthesis and go on
            open = open[:-1]
    # no error: 0 score
    return 0

# calculate the sum of line scores for all lines
# and print it
score = sum([lineScore(line) for line in lines])
print(score)
