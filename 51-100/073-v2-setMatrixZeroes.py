class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # python3.自己的想法是先遍历，如果遇到零就把所在行列非零数都置成负数（我还沾沾自喜的想出 -x**2+x//2 这个置换方法），再遍历一遍将负数变成零。结果样本本身就有负数就歇菜了。看评论好像蛮多人都有这样的思路（什么变小数或者置换成矩阵里没出现过的数）。这样看其实不是题目所需要的，程序推广性不强的。

        # m*n的空间方法应该是再列个矩阵记录每个位置是否是零？m+n的空间方法应该是记录某行和某列是否为零？所以开辟空间记录行列我觉得不行。

        # 热评的方法应该就是题目想要的方法。确实不错。先记录首行和首列是否需置零，然后首行首列来记录是否该列或该行置零（就是没有开辟额外空间记录行列，妙啊。）
        m=len(matrix)
        n=len(matrix[0])
        rowflag,colflag=0,0
        
        for j in range(n):
            if matrix[0][j]==0:
                rowflag=1
                break
                
        for i in range(m):
            if matrix[i][0]==0:
                colflag=1
                break
                
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                    
        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(1,m):
                    matrix[i][j]=0
        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0
        if rowflag:
            for j in range(n):
                matrix[0][j]=0
        if colflag:
            for i in range(m):
                matrix[i][0]=0