class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        # 计算当前数字是“几位数”，把数字按位拆开
        def calculateMagnitude(num):
            if num == 0:return [0]
            result = []
            while num:
                num, tmp = divmod(num, 10)
                result.insert(0,tmp)
            return result
        dic = {0:[1],1:[0,2],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,7],7:[6,8],8:[7,9],9:[8]}
        lowMagnitude = calculateMagnitude(low)
        highMagnitude = calculateMagnitude(high)
        candidates = [0,1,2,3,4,5,6,7,8,9]
        result = []
        # 生成目标“位数”的数字的全部可能组合
        def dfs(result,curMagnitude,targetMagnitude,dic):
            if targetMagnitude == 1: 
                result.insert(0,0) # 如果是目标是1位数，还需要加回来开头的0，直接返回
                return None
            if curMagnitude == targetMagnitude:
                return None
            else:
                currentLen = len(result)
                for i in range(currentLen):
                    item = result.pop(0)
                    for plusChar in dic[item % 10]: # item % 10 拿到末尾数字，然后接上新的数字
                        result.append(item * 10 + plusChar)
                dfs(result,curMagnitude + 1,targetMagnitude,dic)
        allMagnitudeResult = []
        for magnitude in range(len(lowMagnitude),len(highMagnitude) + 1): 
            result = [i for i in range(1,10)] # 此处避免生成的开头有0，初始化为1-9
            dfs(result,1,magnitude,dic) # 默认就是传入1位数的结果
            allMagnitudeResult.extend(result)
        # 由于生成的数组已经排好序，直接拿出开头和结尾即可
        for i in range(len(allMagnitudeResult)):
            if allMagnitudeResult[i] >= low:
                break
        for j in range(len(allMagnitudeResult)-1,-1,-1):
            if allMagnitudeResult[j] <= high:
                break
        return allMagnitudeResult[i:j+1]