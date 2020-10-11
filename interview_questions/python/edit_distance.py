from functools import lru_cache
# https://leetcode.com/problems/edit-distance/

@lru_cache
def minDistance(word1: str, word2: str) -> int:
        print(word1, word2)

        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if word1[-1] == word2[-1]:
            return minDistance(word1[:-1], word2[:-1])
        res = 1 + min(
            minDistance(word1, word2[:-1]),  # insert
            minDistance(word1[:-1], word2[:-1]),  # replase
            minDistance(word1[:-1], word2),
        )
        print(word1, word2, res)
        return res

