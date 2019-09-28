class Solution:
    # 改变了思路，自己的写法完成了官方题解中的思路，能通过更多案例，但还是超时
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur = set()
        res = set()
        for i in range(len(A)):
            # cur表示，以A中第i-1个元素为结尾的result值
            # 每轮循环完成后，cur表示，以A中第i个元素为结尾的result值
            curtmp = set()
            curtmp.add(A[i])
            for curItem in list(cur):
                curtmp.add(A[i] | curItem)
            res = res | curtmp
            cur = curtmp
        return len(res)

# 官方题解能通过，自己实现的话，算法相同，速度稍慢
class Solution(object):
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/bitwise-ors-of-subarrays/solution/zi-shu-zu-an-wei-huo-cao-zuo-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。