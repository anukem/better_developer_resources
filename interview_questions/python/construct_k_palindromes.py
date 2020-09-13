"""Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.



Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s."""

def construct_k_palindromes(s, k):
    if k > len(s):
        return False
    elif k == len(s):
        return True

    seen = {}

    for letter in s:
        seen[letter] = 1 if letter not in seen else seen[letter] + 1

    singles = 0
    doubles = 0
    for key, value in seen.items():
        if value % 2 == 1:
            singles += 1
        doubles += value // 2

    return singles < k <= singles + doubles

# tested on leetcode
