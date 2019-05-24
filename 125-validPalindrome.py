class Solution:
    # 超出时间，其实只要比较一半就可以了，所以会慢
    def isPalindrome(self, s: str) -> bool:
        # 先把字符串把正向和反向列表存下来
        forwardlist = list(s)
        reverselist = list(s[::-1])
        while len(forwardlist)!=0 and len(reverselist)!=0:
            # 去除掉正向列表中的非数字和字母，后面那一串判断是否为数字或者字母
            while len(forwardlist) != 0 and not (65<= ord(forwardlist[0]) <=90 or 97<= ord(forwardlist[0]) <=122 or 48<= ord(forwardlist[0]) <=57) :
                forwardlist.pop(0)
            item1 = forwardlist.pop(0) if len(forwardlist) != 0 else ""
            # 去除掉反向列表中的非数字和字母
            while len(reverselist) != 0 and not (65<= ord(reverselist[0]) <=90 or 97<= ord(reverselist[0]) <=122 or 48<= ord(reverselist[0]) <=57) :
                reverselist.pop(0)
            item2 = reverselist.pop(0) if len(reverselist) != 0 else ""
            # print(item1,item2)
            # 比较两个字符，是否相等
            if item1.lower() != item2.lower():
                return False
        # print(forwardlist,reverselist)
        # 去除掉剩下的非数字和字母
        while len(forwardlist) != 0 and not (65<= ord(forwardlist[0]) <=90 or 97<= ord(forwardlist[0]) <=122 or 48<= ord(forwardlist[0]) <=57) :
            forwardlist.pop(0)
        while len(reverselist) != 0 and not (65<= ord(reverselist[0]) <=90 or 97<= ord(reverselist[0]) <=122 or 48<= ord(reverselist[0]) <=57) :
            reverselist.pop(0)
        # 去除完以后长度不等，则为否
        if len(forwardlist) != len(reverselist):
            return False
        return True
            
            