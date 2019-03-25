class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 参考答案双指针法，左右依次选较短木板逼近
        area = 0
        i = 0
        j = len(height) - 1
        while(i<j):
            area = max((j-i)*min(height[i],height[j]),area)
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return area
        