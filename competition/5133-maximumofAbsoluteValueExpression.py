class Solution:
    # 遍历全部可能性，超时
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        for i in range(len(arr1)):
            for j in range(len(arr1)):
                res = max(abs(arr1[i]-arr1[j]) + abs(arr2[i]-arr2[j]) + abs(i-j),res)
        return res