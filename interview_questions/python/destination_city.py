# https://leetcode.com/problems/destination-city/discuss/850024/Python-Solution-with-comments
def destCity(paths) -> str:
    if len(paths) == 1:
        return paths[0][1]

    # assume that the destination will not lead anywhere
    # so its count should be one

    seen = {}
    for path in paths:
        seen[path[0]] = path[1]

    return [x[1] for x in paths if x[1] not in seen][0]

