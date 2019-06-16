# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 记录从根到该结点的路径 小优化，找到路径就不再继续进行搜索
        def search(root,target):
            def dfs(results,result,node,target):
                if node == target:
                    result.append(node)
                    results.extend(result)
                    return True
                else:
                    if node.left != None:
                        if dfs(results,result+[node],node.left,target):
                            return True
                    if node.right != None:
                        if dfs(results,result+[node],node.right,target):
                            return True
                    return False
            results = []
            dfs(results,[],root,target)
            return results
        plist = search(root,p)
        qlist = search(root,q)
        # 分别得到从根节点到p和q的路径，然后两者相同路径部分的最后一个就是最近公共祖先
        for i in range(min(len(plist),len(qlist))):
            if plist[i] != qlist[i]:
                return plist[i-1]
        return plist[i]