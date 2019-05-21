class Solution:
    # 列表从后往前遍历，加上1进位
    def plusOne(self, digits: List[int]) -> List[int]:
        # flag用来标记是否有进位
        flag = True
        for i in range(len(digits)-1,-1,-1):
            digits[i] = digits[i] + 1
            if digits[i] == 10:
                digits[i] = digits[i] % 10
            else:
                flag = False
                break
        if flag:
            digits.insert(0,1)
        return digits