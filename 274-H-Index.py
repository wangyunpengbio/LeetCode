class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 排序
        citations.sort()
        size = len(citations)
        for i in range(len(citations)):
            if citations[i] >= size - i: # 若当前扫描的元素大于n-i，则表示有n-i个数符合条件，就是答案
                return(size - i)
        return(0)
