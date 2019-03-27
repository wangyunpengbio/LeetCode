# 超出时间限制
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        res = 0
        # 排序以后，直接计算所有两短边之和是否大于长边
        for i in range(len(A)-2):
            for j in range(i + 1,len(A)-1):
                for k in range(j+1,len(A)):
                    if A[i] + A[j] > A[k]:
                        res = max(A[i] + A[j] + A[k],res)
        return res