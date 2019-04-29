class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划，tmp表示当前位置爬有几种方式
        # 初始值的两个为0次和1次，0次表示已经到了的话有0种方法，1次表示剩1个台阶，有一种方法
        # 递推公式为 x[i] = x[i-1] + x[i-2] 当前爬的次数等同于 之前一个台阶的次数 + 之前两个台阶的次数
        x0,x1 = 0,1
        tmp = 0
        for i in range(n):
            tmp = x0 + x1
            # print(x0,x1,tmp)
            x0,x1 = x1,tmp
        return tmp