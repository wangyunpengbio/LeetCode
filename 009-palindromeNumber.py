class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        front = x
        back = 0
        # 将数字的翻转形式计算出来
        while x > 0:
            back = (x % 10) + back * 10
            x = x // 10
        if front == back:
            return True
        else:
            return False