class Solution:
    # 把数组看成链表，找链表环的起始位置
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1
'''
1、第 1 行注释的意思是：“快慢指针”（本文称为“循环解决”，即“检测一个单链表是否存在环”）的做法太 tricky 了，面试官不太希望面试者答出这个方法的原因是：他认为你是有备而来的，你答出了比标准答案还好的答案，但不一定是你真实的水平。

2、鸽子洞原理在很多教材上称之为“抽屉原理”。

作者：LeetCode
链接：https://leetcode-cn.com/problems/two-sum/solution/xun-zhao-zhong-fu-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''