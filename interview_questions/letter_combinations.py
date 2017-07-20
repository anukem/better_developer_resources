def letter_combinations(string):
    combinations = [""]
    digits = { 2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
    
    for i in string:
        i = int(i)
        combos_to_add = []
        for j in combinations:
            array_to_add = add_letters_from_digit(j, i, digits)
            combos_to_add.append(array_to_add)
        for combo in combos_to_add:
            combinations += combo
   
    answer  = []
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
