class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        count = Counter(arr)
        return len(list(count.values())) == len(set(count.values()))