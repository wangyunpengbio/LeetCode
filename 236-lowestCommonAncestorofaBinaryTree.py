# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 超时
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 记录从根到该结点的路径
        def search(root,target):
            def dfs(results,result,node,target):
                if node == target:
                    result.append(node)
                    results.extend(result)
                else:
                    if node.left != None:
                        dfs(results,result+[node],node.left,target)
                    if node.right != None:
                        dfs(results,result+[node],node.right,target)
            results = []
            dfs(results,[],root,target)
            return results
        plist = search(root,p)
        qlist = search(root,q)
        # for item in plist:
        #     print(item.val)
        # for item in qlist:
        #     print(item.val)
        # print(plist)
        # print(qlist)
        # 分别得到从根节点到p和q的路径，然后两者相同路径部分的最后一个就是最近公共祖先
        same = plist[0]
        while len(plist) != 0 and len(qlist) != 0:
            itemP = plist.pop(0)
            itemQ = qlist.pop(0)
            if itemP == itemQ:
                same = itemP
            else:
                break
        return same