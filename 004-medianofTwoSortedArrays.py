class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 没按照题目所述的时间复杂度，直接冰成一个list，排序找中位数
        nums1.extend(nums2)
        nums1.sort()
        numLeng = len(nums1)
        return((nums1[int(numLeng/2)] + nums1[int((numLeng-1)/2)])/2)