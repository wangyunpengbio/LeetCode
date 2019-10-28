class Solution:
    # 格雷编码，然后调整位置
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        for i in range(2 ** n):
            res.append((i >> 1) ^ i)
        for i in range(len(res)):
            if res[i] == start:
                return res[i:] + res[:i]

