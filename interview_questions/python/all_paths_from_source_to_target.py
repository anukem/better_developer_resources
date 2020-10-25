# https://leetcode.com/problems/all-paths-from-source-to-target/submissions/
class Solution:
    def allPathsSourceTarget(graph):
        res = []

        def explore(pathTaken, current, graph):
            if current == len(graph) - 1:
                res.append(pathTaken + [current])
            for path in graph[current]:
                explore(pathTaken + [current], path, graph)

        explore([], 0, graph)
        return res
