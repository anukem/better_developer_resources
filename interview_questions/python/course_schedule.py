# https://leetcode.com/problems/course-schedule/
# The general idea is to use a topological sort to determine whether or not any cycles exist in the graph.
def canFinish(numCourses, prerequisites):
        visited = {}
        def explore(pathTaken, current, mapping):
            for course in mapping.get(current, []):
                if current in pathTaken:
                    return False
                if not explore(pathTaken.union({current}), course, mapping):
                    return False

            [visited.update({x: 1}) for x in pathTaken]
            return True

        mapping = {}
        for pair in prerequisites:
            req, course = pair
            mapping[course] = mapping.get(course, []) + [req]


        for i in range(numCourses):
            if i in visited:
                continue
            elif not explore(set(), i, mapping):
                return False

        return True

