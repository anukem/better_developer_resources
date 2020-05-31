# We have found a map of size n that details out where a series of
# treasures can be located. The coordinates of each treasure are given
# as a string seperated by commas. The two part coordinates consist of
# the top left corner of the treasure, and the bottom right corner of the treasure.
# Treasures are at most 4 cells large and always rectangular. For example, an artifact
# with coordinates 1B 2C looks like this
#
#  A B C D
# 1  1 1
# 2  1 1
# 3
# 4
#
# while a treasure with coordinates 1C 4C looks like this
#
#  A B C D
# 1    1
# 2    1
# 3    1
# 4    1

# given a number n representing the size of the map, and a string representing
# the coordinates of the list, treasures and a list representing the cells that have been raided searched,
# return an int[] where the first entry is the number of treasures that have been searched fully, and the
# second entry is the number of treasures that have been searched partially.

test = [4,"1B 2C,2D 4D","2B 2D 3D 4D 4A"] # should return [1,1]

class Treasure:
    def __init__(self, top_left, bottom_right):
        left_num = top_left[:-1]
        right_num = bottom_right[:-1]
        self.count = 0
        self.parts = set()
        self.parts.add(top_left)
        self.parts.add(bottom_right)

        leftLetter = top_left[-1]
        rightLetter = bottom_right[-1]

        for i in range(int(right_num) - int(left_num)):
            self.parts.add(str(i + int(left_num) + 1) + leftLetter)

        for i in range( ord(rightLetter) - ord(leftLetter) ):
            self.parts.add( left_num + chr(ord(leftLetter) + 1 + i) )



def find_treasure(n, treasure, searched):
    treasure = treasure.split(",")
    treasure = map(lambda x: Treasure(x.split(" ")[0], x.split(" ")[1]), treasure )
    searched = searched.split(" ")
    for i in searched:
        for art in treasure:
            if i in art.parts:
                art.count += 1
    left = 0
    right = 0
    for art in treasure:
        if art.count == len(art.parts):
            left += 1
        elif art.count > 0:
            right += 1

    return [left, right]

print(find_treasure(test[0], test[1], test[2]))
