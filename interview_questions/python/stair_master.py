
# you are climbing a staircase, it takes n steps to reach the top
# each time, you can either climb up 1, 2, or 3 steps.
# How many distinct ways can you climb to the top?

# base case => 1 -> 1
# next case => 2 -> (1, 1), (2)
# next case => 3 -> (1, 1, 1), (1, 2), (2, 1), (3)

base_cases = { 1: 1, 2: 2, 3: 4 }
memo = {}


def unique_ways(n):
    if n in base_cases:
        return base_cases[n]
    if n in memo:
        return memo[n]
    else:
        memo[n] = unique_ways(n - 1) + unique_ways(n - 2) + unique_ways(n - 3)
        return memo[n]


print(unique_ways(1))  # => 1
print(unique_ways(11))  # => 7
print(unique_ways(3))  # => 4
