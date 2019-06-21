class Solution:
    # 超时
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 滑动窗口，依次输出全部可能性
        for i in range(1,len(nums)+1):
            for j in range(0,len(nums)+1-i):
                # print(nums[j:j+i])
                if sum(nums[j:j+i]) >= s:
                    return i
        return 0