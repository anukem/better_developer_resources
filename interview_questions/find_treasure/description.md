We have found a map of size n that details out where a series of
treasures can be located. The coordinates of each treasure are given
as a string seperated by commas. The two part coordinates consist of
the top left corner of the treasure, and the bottom right corner of the treasure.
Treasures are at most 4 cells large and always rectangular. For example, an artifact
with coordinates 1B 2C looks like this

A B C D
1  1 1
2  1 1
3
4

while a treasure with coordinates 1C 4C looks like this

A B C D
1    1
2    1
3    1
4    1

given a number n representing the size of the map, and a string representing
the coordinates of the list, treasures and a list representing the cells that have been raided searched,
return an int[] where the first entry is the number of treasures that have been searched fully, and the
second entry is the number of treasures that have been searched partially.
