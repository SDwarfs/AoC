import statistics

# read lines from file and strip whitespaces at the end
lines = [x.rstrip() for x in open("input.txt")]

# matching closing parenthesis
matching = { '(': ')', '[': ']', '{': '}',  '<': '>'   }
# points for synthax errors with these -missing- closing parenthesis
points   = { ')': 1, ']': 2, '}': 3, '>': 4 }


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
            # if not expected, return 0 score (ignore corrupted lines)
            if c != expected: return 0
            # else: remove correctly closed parenthesis and go on
            open = open[:-1]
    # calculate line score
    score = 0
    # go backwards throuth list (last opened to be closed first)
    for c in reversed(open):
        score *= 5
        score += points[c]
    return score

# get list of all scores
scores = [lineScore(line) for line in lines]
# remove 0 scores (no error)
scores = [x for x in scores if x > 0]
# output median...
print(statistics.median(scores))
