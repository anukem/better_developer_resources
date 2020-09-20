# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) == 1 or len(arr) == 2:
            return True
        distance = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != distance:
                return False

        return True
