class MajorityChecker:
    # 直接调用的内置类Counter
    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        from collections import Counter
        countlist = Counter(self.arr[left:right+1])
        res, freq = countlist.most_common(1)[0]
        if freq >= threshold:
            return res
        else:
            return -1
