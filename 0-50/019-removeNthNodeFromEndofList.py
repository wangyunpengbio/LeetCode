# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''链表前头加一个节点会才能兼容head，这是常规操作'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        headZero = ListNode("Zero")
        headZero.next = head
        tmp = headZero
        # 维护一个list,保存最新加入的n个的节点
        nodelist = [tmp]
        while tmp:
            # print(tmp.val)
            tmp = tmp.next
            nodelist.append(tmp)
            if len(nodelist) > n + 2:
                del nodelist[0]
        # 如果只有一个节点,则直接返回空值
        if len(nodelist) == 2:return []
        nodelist[0].next = nodelist[1].next
        return headZero.next
        