class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 包括 start 和 end 的翻转
        def reverse(nums,start,end):
            for i in range((end-start+1)//2):
                nums[start+i],nums[end-i] = nums[end-i],nums[start+i]
            print(nums)
        N = len(nums)
        k = k % N
        if k == 0:return None
        reverse(nums,0,N-1)
        reverse(nums,0,k-1)
        reverse(nums,k,N-1)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/two-sum/solution/xuan-zhuan-shu-zu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。