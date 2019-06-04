"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        datalist = [] # datalist存储原来链表和新链表的对象，方便加入random指针
        headZero = Node("Zero",None,None)
        # 第一轮遍历,把链表整体构建好
        curNew = headZero
        cur = head
        while cur:
            newNode = Node(cur.val,None,None)
            datalist.append((newNode,cur))
            curNew.next = newNode
            curNew = curNew.next
            cur = cur.next
        # 再遍历一次,加入random
        curNew = headZero.next
        cur = head
        while cur:
            for newItem,oldItem in datalist:  # 其实这里也可以不用datalist存储，原来链表和新链表再搞两个指针从头一起遍历，从而加上random指针也可以
                if oldItem==cur.random:
                    curNew.random = newItem
                # print(newItem==cur,oldItem==cur)
            curNew = curNew.next
            cur = cur.next
        return headZero.next