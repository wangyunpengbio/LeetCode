class Solution:
    # 先转成数字，加一以后再转成列表
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(item) for item in digits]
        num = int("".join(digits))
        num = num + 1
        digits = [int(item) for item in list(str(num))]
        return digits