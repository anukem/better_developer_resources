# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#
# Constraints:
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# Each element of candidate is unique.
# 1 <= target <= 500
# Accepted
# 570,658
# Submissions
# 1,010,629


def dfs(candidates, target, s, curr, ans):
    print(target, s, curr, ans)
    if target == 0:
        ans.append(curr.copy())  # hard copy
        return

    for i in range(s, len(candidates)):
        if candidates[i] > target:
            print(target, s, curr, ans)
            break
        if i > s and candidates[i] == candidates[i - 1]:  # remove duplicates
            print(target, s, curr, ans)
            continue
        curr.append(candidates[i])
        dfs(candidates, target - candidates[i], i + 1, curr, ans)
        curr.pop()


def combinationSum2(candidates, target):
    candidates.sort()
    ans = []
    dfs(candidates, target, 0, [], ans)
    return ans


def combinationSum(candidates, target):
    res = []

    for i in range(len(candidates)):
        val = candidates[i]
        if val == target:
            res += [[val]]
        elif val < target:
            res += [
                [val] + j
                for j in combinationSum(candidates[i + 1 :], target - candidates[i])
            ]

    return res
