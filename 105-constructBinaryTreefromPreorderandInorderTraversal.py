# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Tips: 前序序列拿出根后，就分为左右子树。其中左右子树的组成还是【根，左子树，右子树】，并且前序和中序的左右子树是对应的。
    # 前序遍历：遍历顺序为 父节点->左子节点->右子节点
    # 中序遍历：遍历顺序为 左子节点->父节点->右子节点
    # 所以都是先遍历完“父节点”和“左子节点”，再遍历“右子节点”，所以，前序和中序的左右子树是对应的。
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:]) # 右子树一致
        return root