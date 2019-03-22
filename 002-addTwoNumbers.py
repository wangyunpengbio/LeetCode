class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        r = result
        carry = 0
        # 模拟初等数学直接相加
        while(l1 or l2):
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = carry + a + b # 当前位置的和
            carry = s // 10 # 进几位
            r.next = ListNode(s % 10)
            r = r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return(result.next)