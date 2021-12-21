import timeit
start = timeit.default_timer()
from functools import lru_cache

distr = {}
for roll in [x+y+z for x in range(1,4) for y in range(1,4) for z in range(1,4)]:
    distr[roll] = distr.get(roll, 0) + 1
distr2 = [[roll, distr[roll]] for roll in distr]

@lru_cache(maxsize=None)
def game(p1, p2, turn=1, s1=0, s2=0):
    global distr
    wins = [0,0]
    if turn == 1:
        for roll, count in distr2:
            p_ = (((p1-1) + roll) % 10) + 1
            s_ = s1 + p_
            if s_ >= 21:
                wins[0] += count
            else:
                res = game(p_, p2, 2, s_, s2)
                wins[0] += res[0] * count
                wins[1] += res[1] * count
    else:
        for roll, count in distr2:
            p_ = (((p2-1) + roll) % 10) + 1
            s_ = s2 + p_
            if s_ >= 21:
                wins[1] += count
            else:
                res = game(p1, p_, 1, s1, s_)
                wins[0] += res[0] * count
                wins[1] += res[1] * count
    return wins

print("RESULT:", max(game(7,8)))
end = timeit.default_timer()
print("TIME: ", end-start)
