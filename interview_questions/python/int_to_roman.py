class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        answer = ''

        for index, digit in enumerate(str(num)):
            place = len(str(num)) - index - 1
            answer += self.convert_to_roman(int(digit) * (10**place))
        return answer

    def convert_to_roman(self, num):
        answer = ''
        numerals = [(1, 'I'), (5, 'V'), (10, "X"), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M')]
        sub_nums = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        if (num in sub_nums):
            return sub_nums[num]
        if (num in [x[0] for x in numerals]):
            return list(filter(lambda x: x[0] == num, numerals))[0][1]

        numerals.reverse()
        for index, numeral in enumerate(numerals):
            if (num % numeral[0] == 0):
                if (int(str(num)[0]) > 4):
                    answer += numerals[index - 1][1]
                    num -= numerals[index - 1][0]
                    answer += numerals[index][1]*int((num/numeral[0]))
                    break
                else:
                    answer += numerals[index][1]*int((num/numeral[0]))
                    return answer
        return answer

