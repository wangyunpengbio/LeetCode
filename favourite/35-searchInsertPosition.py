class Solution:
# 强烈建议多读几遍
    def searchInsert(self, nums, target):
    	# 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        if size == 0:
            return 0
        l = 0
        # 如果 target 比 nums里所有的数都大，则最后一个数的索引 + 1 就是候选值，因此，右边界应该是数组的长度
        r = size
		
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
"""
作者：liweiwei1419
链接：https://leetcode-cn.com/problems/two-sum/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""