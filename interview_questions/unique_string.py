# with O(n) time and O(n) space
def unique_chars(s):
    seen = {}
    for letter in s:
        if letter in seen:
            return False
        else:
            seen[letter] = 1
    return True


# O(1) space and O(n^2) time
def unique_chars_constant_space(s):
    for index, letter in enumerate(s):
        for j, let in enumerate(s[1:]):
            print(let, letter)
            if letter == let:
                return False
    return True


print(unique_chars_constant_space( "somethingelse" ))
print(unique_chars_constant_space( "bat" ))
