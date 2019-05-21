# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        cur = dummyHead
        # 类似归并排序中的合并过程
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # 任一为空，直接连接另一条链表
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        return dummyHead.next