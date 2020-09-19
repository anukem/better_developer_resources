# https://leetcode.com/problems/robot-bounded-in-circle/
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        initial = (0 , 0)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0


        for instruction in instructions:
            if instruction == "G":
                move = lambda x, y: (x[0] + y[0], x[1] + y[1])
                initial = move(directions[current_direction], initial)
            elif instruction == "L":
                current_direction = (current_direction - 1) % 4
            elif instruction == "R":
                current_direction = (current_direction + 1) % 4

        if initial == (0, 0) or current_direction != 0:
            return True
        else:
            return False
