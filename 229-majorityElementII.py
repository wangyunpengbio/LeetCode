class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 摩尔投票法
        # n/3最多两个,最少没有
        # 1.找出次数最多的两个数
        # 2.判断各自出现次数 === 时间复杂度为2n -- O(n)，空间复杂度为 O(1)
        m = n = None
        mcount = ncount = 0
        for num in nums:
            if num == m:
                mcount += 1
            elif num == n:
                ncount += 1
            elif not mcount:
                m, mcount = num, 1
            elif not ncount:
                n, ncount = num, 1
            else:
                mcount -= 1
                ncount -= 1
        mcount = ncount = 0
        for num in nums:
            if num == m:
                mcount += 1
            elif num == n:
                ncount += 1
        N = len(nums)
        return [i for i, c in zip((m, n), (mcount, ncount)) if c > N//3]

# 作者：mai-mai-mai-mai-zi
# 链接：https://leetcode-cn.com/problems/two-sum/solution/python-mo-er-tou-piao-fa-by-mai-mai-mai-mai-zi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。