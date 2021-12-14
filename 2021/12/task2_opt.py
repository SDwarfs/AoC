import numpy as np

# read all input lines into lines[] and strip off trailing whitespaces
lines = [x.rstrip() for x in open("input.txt")]


START = 0
END = 1
nodeIDs = { 'start': START, 'end': END }
# nodeNames = [ "start", "end" ]
small = [True, True]
visited = [0, 0]
conn = [[],[]]

def connect(f,t):
    global conn
    if t == START: return # never go back to START
    conn[f].append(t)
    #print(f,"=>", t)

def getNodeID(s):
    if s in nodeIDs:
        return nodeIDs[s]
    nextId = len(nodeIDs)
    visited.append(0)
    conn.append([])
    small.append(s[0] >= 'a' and s[0] <= 'z')
    #nodeNames.append(s)
    nodeIDs[s] = nextId
    return nextId

for line in lines:
    (f,t) = line.split("-")
    f = getNodeID(f)
    t = getNodeID(t)
    connect(f,t)
    connect(t,f)

#print(nodeIDs)
#print(small)
#print(conn)

count = 0
#path = []
def search(p, twiced=False):
    global count, path
    if p == END:
        #for x in path:
        # print(nodeNames[x], end=",")
        # print("end")
        count += 1
        return
    visited[p] += 1
    #path.append(p)
    for c in conn[p]:
        if small[c]:
            if visited[c] == 0: search(c, twiced)
            elif visited[c] == 1 and not twiced: search(c, True)
        else:
            search(c, twiced)
    visited[p] -= 1
    #path = path[:-1]

#print("----------------------------")
search(START)
print(count)
