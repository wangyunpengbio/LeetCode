class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 用队列的想法，把列表整个滤一遍
        flag = 0 # flag记录当前值共有几次
        i = 0 # i记录当前遍历的次数，总共要把整个数组过一遍
        n = len(nums)
        tmp = "" # tmp初始值不等于nums数组中的任何值
        while i < n:
            item = nums.pop(0)
            if item != tmp:
                tmp = item
                flag = 1
            else:
                flag = flag + 1
            # flag记录当前值共有几次，如果超出2次就不再往列表末尾追加
            if flag > 2:
                pass
            else:
                nums.append(item)
            i = i + 1
        return len(nums)