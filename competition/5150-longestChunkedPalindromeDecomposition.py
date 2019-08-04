class Solution:
    # 从左从右向中间找即可
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        left,right = 0,n
        candidates = []
        result = 0
        flagmiddle = False
        while left < right:
            currentLen = 1
            if left == n // 2:
                flagmiddle = True
            while text[left:left+currentLen] != text[right-currentLen:right]:
                if left+currentLen == n // 2:
                    flagmiddle = True
                    currentLen += 1
                    break
                currentLen += 1
            candidates.append(text[left:left+currentLen])
            if flagmiddle:
                result += 1
            else:
                result += 2
            left = left + currentLen
            right = right - currentLen
        return result