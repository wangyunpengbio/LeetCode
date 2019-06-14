# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 改进成用集合存储，查找速度更快，存储A链表的node对象，然后遍历B链表的时候看是否在集合中存在
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        nodelist = set()
        while headA:
            nodelist.add(headA)
            headA = headA.next
        while headB:
            if headB in nodelist:
                return headB
            headB = headB.next
        return None
