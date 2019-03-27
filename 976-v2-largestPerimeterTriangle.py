class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # 一种更简单的方案
        A.sort()
        res = 0
        # 排序以后，从最大的边开始选取，既然选了最大的边， 那么剩下两条边也要尽量的大才能比最大的边更大，并且周长更大
        for i in range(len(A)-3,-1,-1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return res