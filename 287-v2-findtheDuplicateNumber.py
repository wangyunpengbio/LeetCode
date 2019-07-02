class Solution:
    # set集合底层查找是固定时间的 Python 和 Java 都依赖于底层的哈希表，所以插入和查找有固定的时间复杂度
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            """
时间复杂度：O(n)
O(n)。Python 和 Java 都依赖于底层的哈希表，所以插入和查找有固定的时间复杂度。因此，该算法是线性的，因为它由一个执行 NN 次恒定工作的 for 循环组成。
空间复杂度：O(n)
O(n)。在最坏的情况下，重复元素出现两次，其中一次出现在数组索引 n-1n−1 处。在这种情况下，seen 将包含 n-1n−1 不同的值，因此将占用 O(n)O(n) 空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/two-sum/solution/xun-zhao-zhong-fu-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
"""
时间复杂度：O(nlgn)
排序调用在 Python 和 Java 中花费 {O}(nlgn)O(nlgn) 时间，因此它支配后续的线性扫描。
空间复杂度：O(1) (or O(n))，
在这里，我们对 nums 进行排序，因此内存大小是恒定的。如果我们不能修改输入数组，那么我们必须为 nums 的副本分配线性空间，并对其进行排序。

作者：LeetCode
链接：https://leetcode-cn.com/problems/two-sum/solution/xun-zhao-zhong-fu-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
