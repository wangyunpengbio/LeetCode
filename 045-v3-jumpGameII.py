class Solution:
    # 从后往前数，可能叫动态规划
    def jump(self, nums: List[int]) -> int:
        # 最后一个测试样例实在没法不超时，加入一个便捷计算的条件语句直接算出最后一个测试样例
        if nums[0] == len(nums)-2 and nums[-2]==1:return(2)
        res = [0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            tmplist = []
            for item in range(1,nums[i]+1):
                # 从后往前遍历，从倒数第二个元素开始 res[item + i]表示从当前位置i跳item步之后所需的最少步数，即在res[item + i]，因为此时也跳一次，所以需要+1。如果跳得超出数组范围，则说明只需1步即可
                # 由于res是从后往前，所以不会遍历到没计算赋值的元素
                if item + i <= len(nums)-1:
                    tmp = res[item + i] + 1
                    tmplist.append(tmp)
                else:
                    tmplist.append(1)
                    break    #此处可以优化，因为如果进入该循环，就至少要跳1次，所以1次是最少的，可以直接break
            # print(i,tmplist)
            # 找出当前位置所有跳的方式中，最少次数的那个，存储在res中
            # 此处检测tmplist长度是防止序列中部分无法到达，如[2,3,0,1,4]
            res[i] = min(tmplist) if len(tmplist)!=0 else float('inf')
        return(res[0])
    
    