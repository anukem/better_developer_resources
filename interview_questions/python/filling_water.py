# def print_terrain(arr):
#     start = max(arr)
#     start = start[0]
#     while start != -1:
#         layer = ""
#         for i, (terrain, water) in enumerate(arr):
#             if terrain + water >= start and terrain < start:
#                 layer += "W"
#             elif terrain + water < start:
#                 layer += " "
#             else:
#                 layer += "+"
#         print(layer)
#         start -= 1
#
#
# def go_left(arr, pos):
#     num_arr = [x + y for x, y in arr]
#
#     changed = False
#     minimum = pos
#     start = pos
#     while pos != -1:
#         if num_arr[pos] > num_arr[start] or num_arr[pos] > num_arr[pos + 1]:
#             break
#         if num_arr[pos] < num_arr[minimum]:
#             changed = True
#             minimum = pos
#         pos -= 1
#
#     if changed:
#         arr[minimum] = arr[minimum][0], arr[minimum][1] + 1
#     return changed
#
# def go_right(arr, pos):
#     num_arr = [x + y for x, y in arr]
#
#     changed = False
#     minimum = pos
#     start = pos
#     while pos != len(arr):
#         if num_arr[pos] > num_arr[start]:
#             break
#         if num_arr[pos] < num_arr[minimum]:
#             changed = True
#             minimum = pos
#         pos += 1
#
#     if changed:
#         arr[minimum] = arr[minimum][0], arr[minimum][1] + 1
#     return changed
#
#
# def drop_water(arr, pos, amt):
#     while amt != 0:
#         changed = go_left(arr, pos)
#
#         if not changed:
#             changed = go_right(arr, pos)
#
#         if not changed:
#             arr[pos] = (arr[pos][0], arr[pos][1] + 1)
#
#         amt -= 1
#     return arr
#
# def dump_water(terrain, water, location):
#     terrain = [(x, 0) for x in terrain]
#     while water:
#         terrain = drop_water(terrain, location, 1)
#         water -= 1
#     print_terrain(terrain)
# import pytest
#
# def test_1():
#     assert drop_water([(6, 0), (4, 0), (6, 0)], 1, 1) == [(6, 0), (4, 1), (6, 0)]
#
# def test_2():
#     assert drop_water([(6, 0), (4, 0), (3, 0)], 1, 1) == [(6, 0), (4, 0), (3, 1)]
#
# def test_3():
#     assert drop_water([(3, 0), (4, 0), (6, 0)], 1, 1) == [(3, 1), (4, 0), (6, 0)]
#
# pytest.main()
#
#
# dump_water([5, 4, 2,1,2,3,2,1,0,1,2,4], 8, 1)
# print(" ")
#
# dump_water([5, 4, 2,1,2,3,2,1,0,1,2,4], 8, 10)
# print(" ")
#
# dump_water([5, 4, 2,1,2,3,2,1,0,1,2,4], 100, 10)
# print(" ")
#
