# Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning, or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
#
# Example 1:
# Input: [5,3,4,5]
# Output: true
#
#
# Explanation:
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
#
#
# Note:
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.


def can_win(piles, opp_stones=0, my_stones=0, turn=True):
    print("piles is: ", piles)
    if len(piles) == 2:
        val = my_stones + max(piles) > opp_stones + min(piles)
        print("my stones are ",my_stones + max(piles))
        print("opp stones are ",opp_stones + min(piles))
        return val
    if turn:
        left_side = can_win(piles[1:], opp_stones, my_stones + piles[0], False)
        right_side =  can_win(piles[:len(piles) - 1], opp_stones, my_stones + piles[len(piles) - 1], False)
    else:
        left_side = can_win(piles[1:], opp_stones + piles[0], my_stones, turn)
        right_side =  can_win(piles[:len(piles) - 1], opp_stones + piles[len(piles) - 1], my_stones, turn)

    if (left_side or right_side) and turn:
        print('alex will win')
        return True
    else:
        print('alex will lose')
        return False



print(can_win([5, 3, 4, 5]))
