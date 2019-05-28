class Solution:
    # 超出运行时间
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 检查从当前位置开始绕，能否绕一圈
        def circleOK(init,gas,cost):
            gasLeft = gas[init]
            N = len(gas)
            for i in range(1,N+1):
                cur = (init + i) % N
                gasLeft = gasLeft - cost[cur-1]
                if gasLeft < 0:
                    return False
                gasLeft = gasLeft + gas[cur]
                # print(gasLeft)
            return True
        N = len(gas)
        # 每个位置都作为起始试一遍，返回可以绕一圈的出发编号
        for i in range(N):
            if circleOK(i,gas,cost):
                return i
        return -1
# 可以优化的地方在于，不用把每个位置都作为起始试一遍，试得时候，如果 1 起始不行， 2 3 4位置都是消耗>加油，则可以直接跳到5