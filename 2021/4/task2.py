import numpy as np

linenr = 0
lines = [x.rstrip() for x in open("input.txt")]

numbers = [int(x) for x in lines[0].split(",")]


N = (len(lines)-1) // 6
boards = []
boardcounters = np.zeros((N, 10), 'uint8')
for n in range(N):
    board = [[-1,-1,0] for x in range(100)]
    for y in range(5):
        for x in range(5):
            val = int(lines[2+n*6+y][x*3:x*3+2])
            board[val] = [x, y, 1]
    boards.append(board)

boardsdone = [x for x in range(N)]

def increaseCheck(r,n,p):
    boardcounters[n][p] += 1
    if boardcounters[n][p] == 5:
        sum = 0
        for x in range(100):
            if (boards[n][x][2] == 1):
                sum += x
        boardsdone[n] = 1
        print("SUM:", sum, "r:", r, "MULT:", sum*r, "BOARD:", n)
        #exit()

for r in numbers:
    for n in range(N):
        if (boardsdone[n] == 1): continue
        boards[n][r][2] = 0 # mark
        (x,y,m) = boards[n][r]
        if (x>=0):
            increaseCheck(r,n,x)
            increaseCheck(r,n,5+y)
