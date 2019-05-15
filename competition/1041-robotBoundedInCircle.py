class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0,0]
        direction = ['up','right','down','left']
        curDir = 0
        # 循环四次，如果某次可以回到原点，则可以无限循环
        for i in range(4):
            # 按规则行走
            for item in instructions:
                if item == "G":
                    if direction[curDir] == 'up':
                        position[1] = position[1] + 1
                    elif direction[curDir] == 'right':
                        position[0] = position[0] + 1
                    elif direction[curDir] == 'down':
                        position[1] = position[1] - 1
                    elif direction[curDir] == 'left':
                        position[0] = position[0] - 1
                elif item == "L":
                    curDir = (curDir - 1) % 4
                elif item == "R":
                    curDir = (curDir + 1) % 4
            if position[0] == 0 and position[1] == 0:
                return True
        # 如果四次都无法回到原点，则不能无限循环
        if position[0] == 0 and position[1] == 0:
            return True
        else:
            return False