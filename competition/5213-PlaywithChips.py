class Solution:
    # 统计奇数偶数的个数即可
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd,even = 0,0
        for item in chips:
            if item % 2 == 1:
                odd += 1
            else:
                even += 1
        return min(odd,even)