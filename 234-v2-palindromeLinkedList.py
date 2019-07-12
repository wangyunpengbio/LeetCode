# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 数学的方法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s1 = 0
        s2 = 0
        t = 1
        while head:
            s1 = s1*10 + head.val
            s2 = s2 + t*head.val
            t = t * 10
            head = head.next
        return s1 == s2

# 还有一种方法就是，快慢指针找到链表中间；然后翻转后半部分；然后一个从开头，一个从中间，同时比较