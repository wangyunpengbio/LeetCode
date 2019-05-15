# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 链表前头加一个节点会更才能兼容head
        headZero = ListNode("Zero")
        headZero.next = head
        # last保存上一个节点的值
        last = headZero
        cur = headZero.next
        while cur:
            if cur.val == last.val:
                last.next = last.next.next # 如果值重复，则跳过重复元素
            else:
                last = cur
            cur = cur.next
        return headZero.next