# 超出时间限制
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        dummyHead = ListNode(0)
        cur = dummyHead
        cur.next = head
        # 先把整个链表读进来
        numlist = []
        while cur.next != None:
            cur = cur.next
            numlist.append(cur.val)
        # 再对结果赋值 此处可以使用栈数据结构进行优化
        reslist = [0]*len(numlist)
        for i,item in enumerate(numlist):
            for jtem in numlist[i+1:]:
                if jtem > item:
                    reslist[i] = jtem
                    break
        return reslist
                
            