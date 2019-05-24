# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 我们可以通过检查一个结点此前是否被访问过来判断链表是否为环形链表。常用的方法是使用哈希表。
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodesSeen = set()
        while (head != None):
            if head in nodesSeen:
                return True
            else:
                nodesSeen.add(head)
            head = head.next
        return False