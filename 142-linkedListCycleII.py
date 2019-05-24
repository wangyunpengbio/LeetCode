# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 把见过的节点丢集合里，下次再遇见就是环的开始
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = {None}
        while head not in s:
            s.add(head)
            head = head.next
        return head # 如果无环就是None
'''
还有一个纯数学的快慢指针解法，设环的起始节点为 E，快慢指针从 head 出发，快指针速度为 2，设相交节点为 X，head 到 E 的距离为 H，E 到 X 的距离为 D，环的长度为 L，那么有：快指针走过的距离等于慢指针走过的距离加快指针多走的距离（多走了 n 圈的 L） 2(H + D) = H + D + nL，因此可以推出 H = nL - D，这意味着如果我们让俩个慢指针一个从 head 出发，一个从 X 出发的话，他们一定会在节点 E 相遇

				  _____
				 /     \
		 head___________E       \
				\       /
				 X_____/ 
class Solution(object):
    def detectCycle(self, head):
	slow = fast = head
	while fast and fast.next:
	    fast = fast.next.next
	    slow = slow.next
	    if slow == fast:
            break
	else:
	    return None
	while head is not slow:
	    head = head.next
	    slow = slow.next
	return head
'''

# Python的for...else和while...else语法，这是Python中最不常用，最为误解的语法特性之一。

# Python中的for、while循环都有一个可选的else分支(类似if语句和try语句那样），在循环迭代正常完成之后执行。换句话说，如果我们不是除正常以外的其他方式退出循环，那么else分支将被执行。也就是在循环体内没有break语句、没有return语句，或者没有异常出现。

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break # 有回环
        if slow == fast: # 有回环
            while head is not slow:
                head = head.next
                slow = slow.next
            return head # 找环开始的节点
        else:
            return None # 无回环
'''