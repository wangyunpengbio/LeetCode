class Solution:
    # 单调栈
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # 可以保证在最后总会计算
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            print(stack)
            while stack and heights[i] < heights[stack[-1]]: # 当前位置小于栈顶位置时计算
                print("----")
                print(stack)
                s = stack.pop() # 出栈是因为找到右区间了，第i个比你小，那么你的右区间到i-1
                res = max(res,(i-stack[-1]-1)*heights[s]) # i-s[-1]-1 和 i 是 左右边沿
                print((i-stack[-1]-1)*heights[s])
                print(stack)
            stack.append(i)
        return res
