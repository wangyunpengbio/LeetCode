class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        for item in nums1:
            if item in nums2:
                res.append(item)
        return res

# 时间复杂度：O(m+n)O(m+n)，其中 n 和 m 是数组的长度。O(n)O(n) 的时间用于转换 nums1 在集合中，O(m)O(m) 的时间用于转换 nums2 到集合中，并且平均情况下，集合的操作为 O(1)O(1)。
# 空间复杂度：O(m+n)O(m+n)，最坏的情况是数组中的所有元素都不同。
    
# 内置函数的方法
#         set1 = set(nums1)
#         set2 = set(nums2)
#         return list(set2 & set1)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/two-sum/solution/liang-ge-shu-zu-de-jiao-ji-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。