# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        # 先计算链表A的长度，链表B的长度
        cur = headA
        lenA = 0
        lenB = 0
        while cur:
            lenA = lenA + 1
            cur = cur.next
        cur = headB
        while cur:
            lenB = lenB + 1
            cur = cur.next
        # 然后两个链表从头遍历，先把长短对齐。
        nodeA = headA
        nodeB = headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                nodeA = nodeA.next
        if lenA < lenB:
            for i in range(lenB-lenA):
                nodeB = nodeB.next
        # 再同时遍历，两者相遇的地方就是相交节点
        while nodeA:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None