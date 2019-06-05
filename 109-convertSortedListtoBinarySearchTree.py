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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        # 调用和第108题一样的动态规划方法
        def buildBST(nums):
            if len(nums)==0:
                return None
            # 取nums列表的中间下标值
            mid_index = len(nums)//2
            pNode = TreeNode(nums[mid_index])
            pNode.left = buildBST(nums[:mid_index])
            pNode.right = buildBST(nums[mid_index+1:])
            return pNode
        return buildBST(head_list)
