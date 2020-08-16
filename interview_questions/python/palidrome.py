class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        length = length_of_num(x)
        reversed_num = reverse(x, length)
        return True if reversed_num== x else False

        


def length_of_num(x):
    length = 0
    divisor = 1
    while(x / divisor > 0):
        divisor *= 10
        length += 1

    return length 

def reverse(n, length):
    divisor = 10
    reversed_num = 0
    for i in range(0, length ):
        digit = get_digit(n, i)
        reversed_num += digit * 10**(length - i)
    return reversed_num / divisor
    

def get_digit(number, n):
    return number // 10**n % 10

solution = Solution()
print(solution.isPalindrome(211111111111112))
