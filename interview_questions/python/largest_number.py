# # Given a list of non negative integers, arrange them such that they form the largest number.
# #
# # Example 1:
# #
# # Input: [10,2]
# # Output: "210"
# # Example 2:
# #
# # Input: [3,30,34,5,9]
# # Output: "9534330"
# # Note: The result may be very large, so you need to return a string instead of an integer.
# #

#

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

def largestNumber(nums):
    nums = [str(x) for x in nums]
    nums = sorted(nums, key=LargerNumKey)

    return "".join(nums)


print(largestNumber([10, 2]) == "210")
print(largestNumber([0,9,8,7,6,5,4,3,2,1]) == "9876543210")
print(largestNumber([121,12]) == "12121")
print(largestNumber([3, 30, 34, 5, 9]) == "9534330")

