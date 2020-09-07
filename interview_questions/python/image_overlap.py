def get_ones(image):
    res = []
    for i in range(len(image)):
        for j in range(len(image)):
            if image[i][j] == 1:
                res.append((i, j))
    return res

def image_overlap(image1, image2):
    A_ones = get_ones(image1)
    B_ones = get_ones(image2)

    transformation_count = 0
    transformation_map = {}
    for ax, ay in A_ones:
        for bx, by in B_ones:
            vec = (bx - ax, by - ay)
            transformation_map[vec] = 1 if vec not in transformation_map else transformation_map[vec] + 1
            transformation_count = max(transformation_count, transformation_map[vec])

    return transformation_count


# tested on leetcode

