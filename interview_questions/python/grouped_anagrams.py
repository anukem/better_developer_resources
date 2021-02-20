# 49. Group Anagrams
# Medium

# 4265

# 205

# Add to List

# Share
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.


def grouped_anagrams(words):

    grouping = {}
    for word in words:
        word_arr = [_ for _ in word]
        grouping["".join(sorted(word_arr))] = grouping.get(
            "".join(sorted(word_arr)), []
        ) + [word]

    ans = []
    for group in grouping:
        ans.append(grouping[group])

    return ans


def test_1():
    assert grouped_anagrams(["eat", "tea", "ate"]) == [["eat", "tea", "ate"]]


def test_2():
    assert grouped_anagrams(["eat", "tea", "ate", "dot"]) == [
        ["eat", "tea", "ate"],
        ["dot"],
    ]
