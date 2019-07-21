class Solution:
    # 使用字典
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = {}
        for domino in dominoes:
            item = tuple(sorted(domino))
            if item not in res:
                res[item] = [1,0]
            else:
                res[item][1] = res[item][1] + res[item][0]
                res[item][0] = res[item][0] + 1
        resNum = 0
        for value in res.values():
            resNum = resNum + value[1]
        return(resNum)