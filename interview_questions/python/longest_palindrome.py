class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            return s == s[::-1]

        maximum = ""
        def find_largest_palindrome(s):
            i = 0
            j = len(s)


            while j != i:
                current = s[i:j]
                if is_palindrome(current):
                    return current
                j -= 1

            return ""

        if is_palindrome(s):
            return s
        else:
            for i in range(len(s)):
                current = find_largest_palindrome(s[i:])
                if len(current) > len(maximum):
                    maximum = current

        return maximum

