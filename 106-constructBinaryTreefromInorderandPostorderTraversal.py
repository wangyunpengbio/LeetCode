# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Tips: 后序序列拿出根后，就分为左右子树。其中左右子树的组成还是【左子树，右子树，根】，并且中序和后序的左右子树是对应的。
    # 中序遍历：遍历顺序为 左子节点->父节点->右子节点
    # 后序遍历：遍历顺序为 左子节点->右子节点->父节点
    # 所以都是最后遍历完“父节点”和“右子节点”，先遍历“左子节点”，所以，中序和后序的左子树是对应的。
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        else:
            root = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[:index],postorder[:index]) # 左子树一致
            root.right = self.buildTree(inorder[index+1:],postorder[index:-1])
            return root