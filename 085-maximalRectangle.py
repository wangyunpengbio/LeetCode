class Solution:
    # 这一题的算法本质上和84题Largest Rectangle in Histogram一样，对每一行都求出每个元素对应的高度，这个高度就是对应的连续1的长度，然后对每一行都更新一次最大矩形面积。那么这个问题就变成了Largest Rectangle in Histogram。本质上是对矩阵中的每行，均依次执行84题算法。
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] = heights[j] + 1
            res = max(res, self.largestRectangleArea(heights))
        return res

    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                s = stack.pop()
                res = max(res, heights[s] * ((i - stack[-1] - 1) if stack else i))
            stack.append(i)
        return res