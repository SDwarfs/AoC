import numpy as np
import timeit

counter = 0
def dice():
    global dice_idx, counter
    res = dice_idx
    dice_idx = (dice_idx)%100 + 1
    print(res, end=' ')
    counter += 1
    return res

def advance(pos, roll):
    pos -= 1
    pos += roll
    pos = pos % 10
    pos += 1
    return pos

def game(p1, p2):
    global counter
    s1 = 0
    s2 = 0
    winner = 0
    count = 0
    while True:
        roll = dice() + dice() + dice()
        print(" = %d " % (roll), end='=> POS: ')
        print(p1, end=' ')
        p1 = advance(p1, roll)
        #p1 += (p1 + roll - 1) % 10 + 1
        s1 += p1
        print("=>  %d, SCORE: %d " % (p1, s1) )
        if s1 >= 1000:
            winner = 1
            print("RESULT 1", s2 * counter)
            break
        roll = dice() + dice() + dice()
        print(" = %d " % (roll), end='')
        p2 = advance(p2, roll)
        s2 += p2
        print("=> POS: %d, SCORE: %d " % (p2+1, s2) )
        if s2 >= 1000:
            winner = 2
            print("RESULT 1", s1 * counter)
            break
    return winner

dice_idx = 1
winner = game(7,8)
counter = 0
print("WINNER: ", winner)
