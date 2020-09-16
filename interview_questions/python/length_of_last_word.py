# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a maximal substring consisting of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5

def lengthOfLastWord(self, s: str) -> int:
        arr = [x for x in s.split(" ") if x != '']

        if not len(arr):
            return 0
        else:
            return len(arr[len(arr) - 1])


# tested on leetcode
