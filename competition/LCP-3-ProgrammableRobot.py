class Solution:
    # 因为xy都很大，直接模拟会超时，把障碍物映射到最初的一个循环中
    def robot(self, command: str, obstacles, x: int, y: int) -> bool:
        numU = command.count("U")
        numR = command.count("R")
        # 加速运算：如果终点不在移动的矩形内，直接返回False
        if x / (-1 * numR) + y / numU > 1:return False
        if x / numR + y / (-1 * numU) > 1:return False
        from collections import defaultdict
        obstacleDic = defaultdict(list)
        for obstacle in obstacles:
            # 加速运算：可以直接去除掉不在移动的矩形内的障碍
            if obstacle[0] / (-1 * numR) + obstacle[1] / numU > 1:continue
            if obstacle[0] / numR + obstacle[1] / (-1 * numU) > 1:continue
            # 除掉终点以后的障碍
            if obstacle[0] > x or obstacle[0] > y:continue
            timesObs = min(obstacle[0] // numR, obstacle[1] // numU)
            xObs = obstacle[0] - numR * timesObs
            yObs = obstacle[1] - numU * timesObs
            obstacleDic[xObs].append(yObs)
        # 修复如果在循环的开始处有障碍的bug
        if 0 in obstacleDic[0]:return False
        targetTimes = min(x // numR,y // numU)
        x = x - numR * targetTimes
        y = y - numU * targetTimes
        current =  [0,0]
        while True:
            for item in command:
                if item == "R":
                    current[0] += 1
                else:
                    current[1] += 1
                # 有时候终点通过走位的循环映射后，就是(0,0)，所以此处多加一圈
                if current[0] == x + numR and current[1] == y + numU:
                    return True
                # 有时候终点通过走位的循环映射后，就是(0,0)，所以此处多加一圈
                if current[0] > x + numR or current[1] > y + numU:
                    return False
                if current[1] in obstacleDic[current[0]]:
                    return False