res = []
counter = 0

def gen(n, left, right, current):

    global counter
    print(counter)
    counter += 1
    if left == n and right == n:
        res.append(current)
    else:
        if left < n:
            gen(n, left + 1, right, current + "(")
        if left > right:
            gen(n, left, right + 1, current + ")")


gen(3, 0, 0, "")
print(res)
