class Solution:
    # 直接全部挨个计算，超时
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        def calculateOR(nums):
            result = nums[0]
            for item in nums:
                result |= item
            return result
        # B 用于存放所有取“或”运算的值
        B = set()
        for i in range(len(A)):
            for j in range(i,len(A)):
                B.add(calculateOR(A[i:j+1]))
        return len(B)