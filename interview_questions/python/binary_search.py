import timeit

def binary_search(haystack, needle):

    begin = 0
    mid = len(haystack)/2
    end = len(haystack)
    while(begin < end and end - begin != 1):
        if haystack[mid] == needle:
            return "Needle is at position " + str(mid)
        else:
            print(haystack[mid])
            if(haystack[mid] > needle):
                end = mid
                mid = (begin + end) / 2
            else:
                begin = mid
                mid = (begin + end) / 2  
    return "No needle in this haystack" if haystack[mid] != needle else mid 

def main():
    words_file = open("/usr/share/dict/words", "r")
    words = words_file.read().split("\n")
    words = [x.lower() for x in words]
    print(binary_search(words, "dog"))

start = timeit.default_timer()
main()
stop = timeit.default_timer()
print stop - start 


