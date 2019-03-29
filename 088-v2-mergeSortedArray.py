class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 内置函数取巧的方式
        nums1 = sorted(nums1[:m]+nums2)
