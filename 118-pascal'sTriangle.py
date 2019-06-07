class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1,1] for i in range(numRows-1)] # 先把外围的一圈1全都给生成
        res.insert(0,[1])
        for i in range(1,numRows): # 再按照杨辉三角的计算方法，一行行把中间的数字加进去
            for j in range(len(res[i-1])-1):
                res[i].insert(1,res[i-1][j]+res[i-1][j+1])
        return res