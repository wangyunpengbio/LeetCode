class Solution:
    # 从后往前数，可能叫动态规划，超出时间限制 Time Limit Exceeded (TLE)
    def jump(self, nums: List[int]) -> int:
        # res存储了每个位置跳到最后一个元素，最少需要多少次
        res = [0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            tmplist = []
            for item in range(1,nums[i]+1):
                # 从后往前遍历，从倒数第二个元素开始 res[item + i]表示从当前位置i跳item步之后所需的最少步数，即在res[item + i]，因为此时也跳一次，所以需要+1。如果跳得超出数组范围，则说明只需1步即可
                # 由于res是从后往前，所以不会遍历到没计算赋值的元素
                tmp = res[item + i] + 1 if item + i <= len(nums)-1 else 1
                tmplist.append(tmp)
            # print(i,tmplist)
            # 找出当前位置所有跳的方式中，最少次数的那个，存储在res中
            # 此处检测tmplist长度是防止序列中部分无法到达，如[2,3,0,1,4]
            res[i] = min(tmplist) if len(tmplist)!=0 else float('inf')
        return(res[0])
    
    