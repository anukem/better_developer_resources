# Buddy Strings
# Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
#
#
#
# Example 1:
#
# Input: A = "ab", B = "ba"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
# Example 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
# Example 3:
#
# Input: A = "aa", B = "aa"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
# Example 4:
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
#
# Input: A = "", B = "aa"
# Output: false
#
#
# Constraints:
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist of lowercase letters.


def buddy_strings(a, b):
    if a == b:
        return len(set(a)) != len(a)
    elif len(a) != len(b):
        return False
    elif set(a) != set(b):
        return False

    a_map = {x: a.count(x) for x in a}
    b_map = {x: b.count(x) for x in b}

    for key, value in a_map.items():
        if b_map[key] != value:
            return False

    count = 0
    for idx, letter in enumerate(b):
        if letter != a[idx]:
            count += 1

    return count == 2
