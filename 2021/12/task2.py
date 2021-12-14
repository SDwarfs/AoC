import numpy as np

# read all input lines into lines[] and strip off trailing whitespaces
lines = [x.rstrip() for x in open("input.txt")]

conn = {}
visited = {}

nodeIDs = { 'start': 0, 'end': 1 }

def connect(f,t):
    if not f in conn:
        conn[f] = [t]
    else:
        conn[f].append(t)
    visited[f] = 0
    visited[t] = 0
    print(f,"=>", t)

for line in lines:
    (f,t) = line.split("-")
    connect(f,t)
    connect(t,f)

print(conn)
count = 0
def search(p, visited={}, path=[], twiced=False):
    global count
    if p == "end":
        count += 1
        #print("FOUND: ", end='')
        #for x in path:
        #    print(x, end=",")
        #print(p)
        return
    path.append(p)
    visited[p] += 1
    #print(p, visited, path, twiced)
    #conn[p].sort()
    for c in conn[p]:
        if c == "start": continue
        if c[0]>='a' and c[0]<='z':
            if visited[c] == 0:
                search(c, visited, path, twiced)
                continue
            if visited[c] == 1 and not twiced:
                search(c, visited, path, True)
        if c[0]>='A' and c[0] <='Z':
            search(c, visited, path, twiced)
    path = path[:-1]
    #print(path)
    #print(visited)
    #print(twiced)
    #exit()

    visited[p] -= 1

print("----------------------------")
search("start", visited)
print(count)
