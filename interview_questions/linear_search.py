import timeit

def linear_search(haystack, needle):
    for i in haystack:
        if i == needle:
            print("Found needle at position " + str(haystack.index(i)))
            return needle

    return "No needle in this haystack"


def main():
    words_file = open("/usr/share/dict/words", "r")
    words = words_file.read().split("\n")
    words = [x.lower() for x in words]
    print(linear_search(words, "dog"))

start = timeit.default_timer()
main()
stop = timeit.default_timer()
print stop - start 


