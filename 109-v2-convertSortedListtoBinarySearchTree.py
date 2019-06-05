# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 快慢指针法 快慢指针找到链表中心
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        def buildBST(head,tail):
            if head == tail:
                return None
            fast = head
            slow = head
            # 此处是为了获得链表的中间结点，即slow
            while fast.next != tail and fast.next.next != tail:
                fast = fast.next.next
                slow = slow.next
            # 如果是偶数长度的链表，slow为中间较小的那个
            pNode = TreeNode(slow.val)
            pNode.left = buildBST(head,slow)
            pNode.right = buildBST(slow.next,tail)
            return pNode
        return buildBST(head,None)
