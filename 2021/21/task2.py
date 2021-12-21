import timeit
start = timeit.default_timer()

def advance(pos, roll):
    pos -= 1
    pos += roll
    pos = pos % 10
    pos += 1
    return pos

distr = {}
for x in range(1,4):
    for y in range(1,4):
        for z in range(1,4):
            sum = x+y+z
            if not sum in distr: distr[sum] = 0
            distr[sum] += 1

distr2 = []
for x in distr:
    distr2.append([x, distr[x]])
n_distr = len(distr2)

def game(p1, p2, turn=1, s1=0, s2=0):
    global distr, winner
    if turn == 1:
        for i in range(n_distr):
            roll, count = distr2[i]
            p_ = advance(p1, roll)
            s_ = s1 + p_
            if s_ >= 21:
                sum[0] += count
                # winner[0] += universes * count
            else:
                res = game(p_, p2, 2, s_, s2)
                sum[0] += res[0] * count
                sum[1] += res[1] * count
    else:
        for i in range(n_distr):
            roll, count = distr2[i]
            p_ = advance(p2, roll)
            s_ = s2 + p_
            if s_ >= 21:
                winner[1] += universes * count
            else:
                game(p1, p_, 1, s1, s_, universes*count)

#game(4,8)
game(7,8)
print("WINNER: ", max(winner))
end = timeit.default_timer()
