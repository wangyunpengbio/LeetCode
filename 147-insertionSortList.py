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
        cur = head
        nodelist = [headZero]
        while cur:
            if cur.val < nodelist[-1].val:
                nodelist[-1].next = cur.next
                for i in range(len(nodelist)):
                    if nodelist[i].val > cur.val:
                        nodelist[i-1].next = cur
                        cur.next = nodelist[i]
                        nodelist.insert(i,cur)
                        break
                cur = nodelist[-1].next
            else:
                nodelist.append(cur)
                cur = cur.next
        return headZero.next