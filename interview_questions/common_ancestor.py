



#Write a function that, for two given individuals in our dataset, returns true if and only if they share at least one known ancestor.

# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   9

#Sample input and output:
#[3, 8] => false
#[5, 8] => true
#[6, 8] => true


class Node:

    def __init(self, name)__:
        self.name = name
        self.parents = []

    def addParent(self, value):
        self.parents.append(value)

    def lineage(self):
        lineage = []
        if self.hasParents() == False:
            return []
        else:
            while(parent.hasParents()):
                lineage.append(parent.parents)
                for parent in parent.parents:
                    lineage.append(lineage(parent))

    def hasParents(self):
        return True if len(self.parents) > 0 else False


def common_ancestor(parentChildPairs, children):
    people = []

    for pair in parentChildPairs:
        child = pair[1]
        parent = pair[0]

        if child not in people:
            kid = Node(child)
            kid.addParent(parent)
        else:
            index = people.index(kid)
            people[index].addParent(parent)


    child1 = people[people.index(children[0])]
    child2 = people[people.index(children[1])]

    for parent in child1.parents:
        if parent in child2.lineage():
            return True

    return False



print(common_ancestor(parentChildPairs, [3, 8]))
