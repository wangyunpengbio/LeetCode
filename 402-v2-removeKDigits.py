class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
# 找到拐点，去除拐点即可
# 单调栈的另一个应用，思想为删除靠前的较大的数能够使得最后的数值最小。 构建递增栈，若当前数字小于栈顶元素，则在满足待删减字符数不为0的情况下，栈顶元素出栈，当前数字入栈。
# 思路分析：
#     我们先举几个栗子，当输入num = "125324", k = 1时，输入的结果是“12324”，删除的是'5'
#     当输入num = "125324", k = 2时，先删除的是'5'，得到“12324”，再删除'3'，就是结果“1224”
#     当输入num = "125324", k = 3时，先删除的是'5'，得到“12324”，再删除'3'，得到“1224”，最后删除末尾的'4'得到结果"122"
        nums = list(num)
        # i表示已经删除的元素个数，总共要删掉k个元素
        i = 0
        j = 0
        # 如果nums[j] > nums[j+1] 则表示拐点
        while j + 1 < len(nums) and i < k:
            # print(nums,j)
            if nums[j] > nums[j+1]:
                nums.pop(j)
                i = i + 1
                j = j - 2 # 由于pop了一个元素，新的j元素没有与此时的j-1比较，所以要j=j-2
            j = max(j + 1, 0) # 如果之前是删了第一个元素，就不用再往前挪了，最少也要是0
        # print(nums)
        # 如果当前元素没删够k个元素,则从后往前删满为止
        while i < k:
            nums.pop(-1)
            i = i + 1
        # print(nums)
        # 去除掉先导0
        while len(nums) > 0 and nums[0] == "0":
            nums.pop(0)
        if len(nums) == 0:
            return "0"
        return "".join(nums)
