class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        numstmp = list(nums1)
        i = 0
        j = 0
        # whetherlist表示排序好的结果list中每个元素依次源于哪儿个list
        whetherlist = []
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                whetherlist.append("1")
                i = i + 1
            else:
                whetherlist.append("2")
                j = j + 1
        while i<m:
            whetherlist.append("1")
            i = i + 1
        while j<n:
            whetherlist.append("2")
            j = j + 1
        # 依次按照whetherlist将元素塞回原始list
        k = 0
        while k<m+n:
            if whetherlist[k] == "1":
                nums1[k] = numstmp[0]
                del numstmp[0]
            else:
                nums1[k] = nums2[0]
                del nums2[0]
            k = k + 1
