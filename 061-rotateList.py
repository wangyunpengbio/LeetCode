# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        rawhead = ListNode(None)
        rawhead.next = head
        rawtail = ListNode(None)
        # 先计算共有多少个节点，并且把原来的末尾节点保存下来
        length = 0
        while(head):
            length = length + 1
            rawtail = head
            head = head.next
        if length == 0: return rawhead.next # 本身是空链表，则不需要旋转
        k = k % length
        if k == 0: return rawhead.next # 如果余数为0，则不需要旋转
        # 如果需要旋转，则先把末尾连上开头，变成一个环
        rawtail.next = rawhead.next
        for i in range(length - k):
            rawhead = rawhead.next
        # 新的开头就是下一个对象，所以把下一个对象保存下来
        newhead = rawhead.next
        # 把下一个对象置空值
        rawhead.next = None
        return newhead