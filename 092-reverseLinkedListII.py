# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 用一个栈把要翻转的部分存下来，然后依次弹出连起来
        stack = []
        headZero = ListNode("zero")
        headZero.next = head
        cur = headZero
        flag = True
        i = 0
        while cur and flag:
            if i == m - 1: # 记录翻转开始之前的那个节点
                start = cur
            while m <= i <= n:
                stack.append(cur)
                i = i + 1
                cur = cur.next
                flag = False # 停止外部循环,停止前因为i = n+1，所以还会向后挪一个记录末尾值
            if i == n + 1: # 记录翻转结束之后的那个节点
                end = cur
            if cur: # 这个if是防止翻转结束在链表末尾，末尾节点空了会报错
                cur = cur.next
                i = i + 1
        # for item in stack:  # 检查现在链表的值
        #     print(item.val)
        # print(start.val,end.val)
        while stack:
            start.next = stack.pop()
            start = start.next
        start.next = end
        return headZero.next