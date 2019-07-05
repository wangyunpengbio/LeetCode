class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        start,count = 0,0
        while count < N:
            current = start
            prev = nums[start]
            while True:
                nextIndex = (current + k) % N
                temp = nums[nextIndex]
                nums[nextIndex] = prev
                prev = temp
                current = nextIndex
                count += 1
                if current == start:
                    break
            start += 1
# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/two-sum/solution/xuan-zhuan-shu-zu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。