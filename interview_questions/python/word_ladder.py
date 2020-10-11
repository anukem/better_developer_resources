# https://leetcode.com/problems/word-ladder/submissions/
def ladder_length(beginWord, endWord, wordList):
    graph = {}
    for word in wordList:
        for i in range(len(word)):
            neighbor = word[0:i] + "_" + word[i + 1 :]
            graph[neighbor] = graph.get(neighbor, []) + [word]

    queue = []

    queue.append((beginWord, 0))

    if endWord not in wordList:
        return 0

    visited = set()
    while len(queue):
        current, level = queue.pop(0)
        if current == endWord:
            return level + 1

        for i in range(len(current)):
            neighbor = current[0:i] + "_" + current[i + 1 :]
            for next_word in graph.get(neighbor, []):
                if next_word not in visited:
                    visited.add(current)
                    queue.append((next_word, level + 1))
    return 0
