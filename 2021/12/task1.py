import numpy as np

# read all input lines into lines[] and strip off trailing whitespaces
lines = [x.rstrip() for x in open("input.txt")]

conn = {}

def connect(f,t):
    if not f in conn:
        conn[f] = [t]
    else:
        conn[f].append(t)
    print(f,"=>", t)

for line in lines:
    (f,t) = line.split("-")
    connect(f,t)
    connect(t,f)

print(conn)
count = 0
def search(p, visited={}, path=[]):
    global count
    if p == "end":
        count += 1
        print(path)
        return
    path.append(p)
    visited[p] = 1
    for c in conn[p]:
        if c[0]>='a' and c[0]<='z' and (c in visited) and (visited[c] == 1): continue
        search(c, visited, path)
    visited[p] = 0
    path.remove(p)

search("start")
print(count)
