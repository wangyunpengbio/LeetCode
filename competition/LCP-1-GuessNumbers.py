class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        res = 0
        for i in range(3):
            if guess[i] == answer[i]:
                res = res + 1
        return res