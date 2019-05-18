# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 递归
        N = len(nums)
        # print(N)
        if N == 0:
            return None
        else:
            left = 0 # 左边元素的索引
            right = N - 1 # 右边元素的索引
            mid = (left + right + 1) // 2 # 正中间元素的索引(如果是2个元素，正中间元素为后面那个)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[left:mid]) # 左边数组(不包括中间元素)
            root.right = self.sortedArrayToBST(nums[mid + 1:right + 1]) # 右边数组(不包括中间元素)
            return root