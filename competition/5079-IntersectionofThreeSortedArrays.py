class Solution:
    # 直接计数，统计出现三次的数字即可
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr1.extend(arr2)
        arr1.extend(arr3)
        from collections import Counter
        obj = Counter(arr1)
        res = []
        for k in sorted(obj):
            if obj[k] == 3:
                res.append(k)
        return res