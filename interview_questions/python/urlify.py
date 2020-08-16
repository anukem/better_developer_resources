# given a string and length, add '%20' to all the spaces

def urlify(s, length):
    s = s[:length]
    s = s.split(" ")
    s = "%20".join(s)
    return s

print(urlify("d f s f ", 7))
print(urlify("something      ", 9))

