# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 使用两个临时头节点，将大于X的保存在less_head，将大于等于X的保存于more_head，再把二者连接起来。
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(0)
        answer1 = dummy1
        dummy2 = ListNode(0)
        answer2 = dummy2
        if head:
            while head:
                if head.val<x:
                    dummy1.next = head                    
                    dummy1 = dummy1.next
                     
                else:
                    dummy2.next = head
                    dummy2 = dummy2.next
                head=head.next
        else:
            return []
        dummy1.next = answer2.next
        dummy2.next = None # dummy2的最后next要置空，不然链表会循环
        return answer1.next