def point_to_position(x, y, m):
    return (x*m) + y

def position_to_point(pos, m):
    x = pos // m
    y = pos % m

    return x, y

def search_matrix(matrix, target):

    if not matrix or not matrix[0]:
        return False

    def find_value(minimum, maximum):

        x_min, y_min = minimum
        x_max, y_max = maximum

        m = len(matrix[0])
        pos1 = point_to_position(x_min, y_min, m)
        pos2 = point_to_position(x_max, y_max, m)

        if pos1 > pos2:
            return False

        mid_position = (pos1 + pos2) // 2

        x_mid, y_mid = position_to_point(mid_position, m)


        mid = x_mid, y_mid
        if matrix[x_mid][y_mid] == target:
            return True
        elif matrix[x_mid][y_mid] > target:
            return find_value(minimum, position_to_point(mid_position - 1, m))
        elif matrix[x_mid][y_mid] < target:
            return find_value(position_to_point(mid_position + 1, m), maximum)

    return find_value((0, 0), (len(matrix) - 1, len(matrix[0]) - 1))
return search_matrix(matrix, target)

