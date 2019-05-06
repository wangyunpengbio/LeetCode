# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 链表前头加一个节点会更才能兼容head
        headZero = ListNode("Zero")
        headZero.next = head
        cur = headZero.next
        stack = [headZero]
        # flag表示当前是否需要把重复的数据排出
        flag = False
        while cur:
            if cur.val != stack[-1].val:
                # 如果栈顶元素是重复的，需要把栈顶的元素排掉，不然后面写的stack[-2]会指向重复的元素
                if flag:
                    stack.pop()
                    flag = False
                stack.append(cur)
            else: # 如果当前值和栈顶的值一样，则栈倒数第二个元素后接当前元素的下一个
                  # 并且说明，栈顶元素是重复的，下一波遇到新元素需要排出栈顶元素
                stack[-2].next = cur.next
                flag = True
            # print(cur.val)
            cur = cur.next
        return headZero.next
