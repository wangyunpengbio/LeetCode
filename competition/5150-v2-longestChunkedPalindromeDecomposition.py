class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        l, r = 0, n
        cands = []
        cnt = 0
        while l < r:
            len_ = 1
            while text[l:l+len_] != text[r-len_:r]:
                len_ += 1
            cands.append(text[l:l+len_])
            if l == r - len_:
                cnt += 1
            else:
                cnt += 2
            l += len_
            r -= len_
        return cnt