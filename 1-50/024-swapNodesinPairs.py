# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        res = pre
        # 用图画出每个节点的名字，以及线就可以了
        while head and head.next:
            # 给线赋值
            pre.next = head.next
            head.next = head.next.next
            pre.next.next = head
            # 当前节点名转移
            pre = pre.next.next
            head = head.next
        return res.next
        