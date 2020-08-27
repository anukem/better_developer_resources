# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


def letter_combinations(string):
    combinations = [""]
    digits = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    for i in string:
        i = int(i)
        combos_to_add = []
        for j in combinations:
            array_to_add = add_letters_from_digit(j, i, digits)
            combos_to_add.append(array_to_add)
        for combo in combos_to_add:
            combinations += combo

    answer = []
    for i in combinations:
        if len(i) == len(string):
            answer.append(i)
    return answer


def add_letters_from_digit(word, digit, dictionary):
    answer = []
    for i in dictionary[int(digit)]:
        answer.append(word + i)

    return answer


print(letter_combinations("2532"))
