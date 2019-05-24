# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 双指针：通过使用具有 不同速度 的快、慢两个指针遍历链表，空间复杂度可以被降低至 O(1)O(1)。慢指针每次移动一步，而快指针每次移动两步。
    def hasCycle(self, head):
        if (head == None or head.next == None):
            return False
        slow = head
        fast = head.next
        while fast != None:
            slow = slow.next
            fast = fast.next
            if fast == None: # 如果快指针已经到末尾，则直接跳出循环，返回false
                break
            fast = fast.next # 没到末尾才继续往下一个挪
            if slow == fast:
                return True
        return False