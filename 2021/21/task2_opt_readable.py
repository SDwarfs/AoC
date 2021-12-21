from functools import lru_cache

# calculate the absolute frequency of the sum of 3 dice rolls
# with a 3 sided die. distr[]
freq = {}
for rolled_sum in [x+y+z for x in range(1,4) for y in range(1,4) for z in range(1,4)]:
    freq[rolled_sum] = freq.get(rolled_sum, 0) + 1
# convert the dictionary into a list for easier handling:
freq_list = [[rolled_sum, freq[rolled_sum]] for rolled_sum in freq]

# we use a caching decorator, to compute every recursion variant only once
# all further calls with the same parameters are looked up in the lru_cache
# Note: there are only: ~90'000 (=10*10*2*21*21) possible game states,
# where no player has yet won...
@lru_cache(maxsize=None)
# @p1 and @p2 are the current positions of the players on the board
# @turn tells whos players turn it is (0 = player 1, 1= player 2)
# @s1 and @s2 are the current score of player 1 and player 2
# @return - the function returns an array containing the count of wins
# for player 1 and player 2.
def game(p1, p2, turn=0, s1=0, s2=0):
    # reset the counters to 0 for both player
    wins = [0, 0]
    # who's player is next after this turn, used for recursive calls later
    next_turn = (turn + 1) % 2
    # go through all posible 3-dice-rolls-sum outcomes and their
    # absolute frequencies
    for rolled_sum, freq in freq_list:
        # We use temporary variables for new positions so we don't have to
        # restore them after the loop's end. Also arrays to allow access
        # to the current players values by indexing.
        p = [p1, p2]
        s = [s1, s2]
        # advance current player's position according to rolled_sum
        # note that player positions are 1 .. 10, hence we subtract 1
        # first and add 1 later. We cannot use 0..9 or we had to do tricks
        # when calcuting the score instead.
        p[turn] = (((p[turn] - 1) + rolled_sum) % 10) + 1
        # increase current player's score by the new position
        s[turn] += p[turn]
        # check if the current player had won for that outcome
        if s[turn] >= 21:
            # the score is 21 or above, so the current player won 'freq' times
            # in this recursion branch for this dice roll outcome...
            wins[turn] += freq
        else:
            # we don't know the outcome yet, so we call the function
            # rescursively for the new game state to calculate the
            # outcomes for both players
            res = game(p[0], p[1], next_turn, s[0], s[1])
            # for the current game state there are freq variants leading
            # to this new game state, hence multiply freq by the returned
            # number of wins and add them to the outcome list
            wins[0] += res[0] * freq
            wins[1] += res[1] * freq
    # return the number of won games [player1, player2] for this game state
    return wins

# calculate the number of wins for player1/player1 given their start positions
wins = game(7, 8)
# the requested result is the higher number of both...
print("RESULT:", max(wins))
