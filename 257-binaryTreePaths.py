# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 深度优先遍历，每次传递的result进行追加，result本身同一层不追加
        def dfs(results,result,node):
            if node.left == None and node.right == None:
                result = result+[str(node.val)]
                results.append(result[:])
                return None
            else:
                if node.left != None:
                    dfs(results,result+[str(node.val)],node.left)
                if node.right != None:
                    dfs(results,result+[str(node.val)],node.right)
        if root == None:return []
        results = []
        dfs(results,[],root)
        return ["->".join(item) for item in results]