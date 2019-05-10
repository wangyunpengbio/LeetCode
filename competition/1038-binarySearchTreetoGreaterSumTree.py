# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 相当于中序遍历，逆向累加求和，再赋值回去
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 中序遍历
        def inorderTraversal(root: TreeNode) -> List[int]:
            res = []
            if not root: # 如果根是空的话
                return []
            else:
                res.extend(inorderTraversal(root.left))
                res.append(root.val)
                res.extend(inorderTraversal(root.right))
                return res
        # 中序遍历结果存在res中
        res = inorderTraversal(root)
        # 中序遍历累加
        for i in range(len(res)-2,-1,-1):
            res[i] = res[i] + res[i+1]
        # 赋值
        def applyInorderTraversal(root: TreeNode,res,level):
            if root == None: # 如果根是空的话
                pass
            else:
                applyInorderTraversal(root.left,res,level)
                root.val = res[level[0]]
                level[0] = level[0] + 1
                applyInorderTraversal(root.right,res,level)
        level = [0]
        applyInorderTraversal(root,res,level)
        return root
