# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 把第一棵树的值存下来，搜第二棵树的时候，找目标即可
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def inorderTraversal(root):
            if root == None:
                return []
            else:
                return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
        tree1Values = set(inorderTraversal(root1))
        def search(root,treeValues,target):
            if root == None:
                return False
            else:
                return search(root.left,treeValues,target) | ((target - root.val) in treeValues) | search(root.right,treeValues,target)
        return search(root2,tree1Values,target)