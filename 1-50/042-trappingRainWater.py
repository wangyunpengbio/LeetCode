class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            # 如果当前柱子比栈顶柱子高
            while stack and height[i] > height[stack[-1]]:
                # j为当前的坑底，前一根柱子变为栈顶柱子
                j = stack.pop()
                if stack: # 弹出元素当坑底后，如果栈空了，则没有柱子了
                    # 此个小坑的高度，为“栈顶柱子”和“当前柱子”中较矮的柱子，再减去坑的高度
                    # 宽度为“栈顶柱子”和“当前柱子”间的距离
                    tmpheight = min(height[i],height[stack[-1]]) - height[j]
                    tmpwidth = i-stack[-1]-1
                    res = res + tmpheight * tmpwidth
            stack.append(i)
        return res