class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 暴力法，遍历全部容器
        area = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                area = max((j-i)*min(height[i],height[j]),area)
        return area
        