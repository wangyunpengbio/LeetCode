class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
    # 测试用例[-1,4,2,1,9,10]
    # 遍历一次数组把大于等于1的和小于数组大小的值放到原数组对应位置，然后再遍历一次数组查当前下标是否和值对应，如果不对应那这个下标就是答案，否则遍历完都没出现那么答案就是数组长度加1。
    
    # 输入数组为未排序数组，要求找到其中最小的正整数，很自然地想到先排序、再查找
    # 但本题要求时间复杂度为O(n)，因此不能使用最坏情况下复杂度为O(nlogn)的CBA式排序算法
    # 基于散列表的桶排序能满足时间复杂度O(n)的要求，但需要额外O(M)的空间来构建散列表，不满足空间复杂度为O(1)的要求
    # 因此只能采用时间换空间的方法，就地(in place)构建散列表，即在原数组内部构建散列表
    # 不需要额外O(M)的空间，但为了在就地构建散列表时，能不丢失原数组的数据信息，需要额外的时间复杂度至多为O(n)的交换(swap)操作
    # 分析至此，解题方法就简化为：就地桶排序，再查找
        # 就地构建散列表
        for i in range(len(nums)):
            # 被hash的数字范围为[1, nums.size()], hash表长度nums.size()
            # hash函数为hash(n) = n - 1, 即对于输入数组中每一个处于hash范围内的数n，将其就地hash到下标为n - 1的桶单元
            # 注意此处最后一个判断不能写成：nums[i] - 1 != i，二者不仅形式不同，其含义和结果都不同
            # 此处while循环相当于循环直到把第i个元素排好了
            while 1<=nums[i]<=len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
            # print(nums)
        i = 0
        while i < len(nums):
            if nums[i]!=i+1:
                break
            i = i + 1
        # print(i)
        return i + 1