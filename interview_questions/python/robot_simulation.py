# https://leetcode.com/problems/walking-robot-simulation/submissions/

def robot_sim(paths, obstacles):
    seen = set()
    [seen.add((x[0], x[1])) for x in obstacles]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    current_direction = 0
    end = (0, 0)
    max_distance = 0

    for path in paths:
        while path > 0:
            add = lambda x, y : (x[0] + y[0], x[1] + y[1])
            sub = lambda x, y : (x[0] - y[0], x[1] - y[1])
            end = add(end, directions[current_direction])

            if end in seen:
                end = sub(end, directions[current_direction])

            path -= 1

        if path == -1:
            current_direction += 1
        elif path == -2:
            current_direction -= 1

        current_direction = current_direction % len(directions)

        max_distance = max(max_distance, end[0]**2 + end[1]**2 )

    return max_distance


