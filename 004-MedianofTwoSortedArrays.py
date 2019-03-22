class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numslen1 = len(nums1)
        numslen2 = len(nums2)
        numLeng = numslen1 + numslen2
        nums1.extend(nums2)
        nums1.sort()
        return((nums1[int(numLeng/2)] + nums1[int((numLeng-1)/2)])/2)