# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
#     实现思路 ：以1->2->3->4->5, m = 2, n=4 为例:
#     定位到要反转部分的头节点 2，head = 2；前驱结点 1，pre = 1；
#     当前节点的下一个节点3调整为前驱节点的下一个节点 1->3->2->4->5,
#     当前结点仍为2， 前驱结点依然是1，重复上一步操作。。。
#     1->4->3->2->5.
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        headZero = ListNode("zero")
        headZero.next = head
        pre = headZero
        for i in range(1,m): # 定位到要反转部分的头节点，pre最后为开始翻转的前驱
            pre = pre.next
        cur = pre.next
        for i in range(m,n):
            nextNode = cur.next
            cur.next = nextNode.next
            nextNode.next = pre.next
            pre.next = nextNode
        return headZero.next