# Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def is_palindrome_permutation(s):
    seen = {}

    for index, letter in enumerate(s):
        if letter not in seen:
            seen[letter] = 1
        else:
            seen[letter] += 1

    count = 0
    for key in seen:
        if seen[key] % 2 != 0:
            count += 1

    return count < 2



print(is_palindrome_permutation("something"))  # => False
print(is_palindrome_permutation("osso"))  # => True
print(is_palindrome_permutation("octcoc"))  # => False
