# You're given two string a and b.
# Your job is to construct b using subsequences of a.
# If its not possible return -1, otherwise, return the shortest number
# of subsequences to get to b.

# Example 1: "abd" "ad" => 1
# Example 2: "abx" "be" => -1
# Example 3: "ababa" "bbba" => 2


def trim_one_path(ss, s):
    ss_stack = [x for x in reversed(ss)]
    print(ss_stack)
    idx = 0
    while len(ss_stack) and s:
        if ss_stack[-1] == s[idx]:
            s = s[idx + 1 :]
        ss_stack.pop()

    return s


def shortest_way(ss, s):
    if not set(ss).issuperset(set(s)):
        return -1

    ans = 0
    while len(s):
        s = trim_one_path(ss, s)
        ans += 1
    return ans


print(shortest_way("abc", "abdcb"))
