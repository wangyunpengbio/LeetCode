# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        N = len(arr)
        for i in range(N//2):
            if arr[i] != arr[N-1-i]:
                return False
        return True