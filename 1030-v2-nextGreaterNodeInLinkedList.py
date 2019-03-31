# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 先把整个链表读进来
        numlist = []
        while head!=None:
            numlist.append(head.val)
            head = head.next
        # 再对结果赋值
        n = len(numlist)
        reslist = [0 for i in range(n)]
        stack = [] # 使用栈结构，只用遍历依次即可
        for i,item in enumerate(numlist):
            print(stack)
            if not stack:
                stack.append(i)
                continue
            while stack and numlist[i]>numlist[stack[-1]]:
                p = stack.pop()
                reslist[p] = numlist[i]
            stack.append(i)
        return reslist