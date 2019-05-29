# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 使用辅助数组进行插入排序
        headZero = ListNode(float("-inf"))
        headZero.next = head
        cur = head # 当前循环的节点
        pre = headZero # 前驱节点
        while cur:
            if cur.val < pre.val:
                pre.next = cur.next
                tmppre,tmpcur = headZero,headZero.next# 此处注意head一直指向最原始的头节点，应该用动态的头结点headZero.next
                while tmpcur:
                    if tmpcur.val > cur.val:
                        break
                    tmppre = tmppre.next
                    tmpcur = tmpcur.next
                tmppre.next = cur
                cur.next = tmpcur
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
        return headZero.next