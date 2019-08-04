# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 找到给定节点；算出给定节点左子树下面的节点总数，算出给定节点右子树下面的节点总数，由整棵树的节点数量减去上述两部分，得到剩下节点数，判断这三部分最大的，是否大于剩下两部分之和
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def calnodes(root):
            nodeSum = 0
            queue = []
            queue.append(root)
            while len(queue)!=0:
                item = queue.pop(0)
                if item == None:
                    pass
                else:
                    nodeSum += 1
                    queue.append(item.left)
                    queue.append(item.right)
            return nodeSum
        queue = []
        queue.append(root)
        while len(queue)!=0:
            item = queue.pop(0)
            if item == None:
                pass
            elif item.val == x:
                break
            else:
                queue.append(item.left)
                queue.append(item.right)
        rightSum = calnodes(item.right)
        leftSum = calnodes(item.left)
        threeParts = [rightSum,leftSum,n-rightSum-leftSum-1]
        threeParts.sort()
        if threeParts[0] + threeParts[1] + 1 < threeParts[2]:
            return True
        else:
            return False