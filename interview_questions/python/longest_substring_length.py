# 3. Longest Substring Without Repeating Characters
# Medium
#
# 10909
#
# 617
#
# Add to List
#
# Share
# Given a string s, find the length of the longest substring without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0
#
def longest_substring_length(s):
    seen = {}
    if not len(s):
        return 0

    longest = 1

    i, j = 0, 0

    seen[s[i]] = 0

    while j != len(s):
        if i == j:
            j += 1
            continue

        if s[j] in seen:
            i = seen[s[j]] + 1 if seen[s[j]] + 1 > i else i

        longest = max(longest, j - i + 1)
        seen[s[j]] = j
        j += 1

    return longest

