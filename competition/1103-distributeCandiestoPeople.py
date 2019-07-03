class Solution:
    # 暴力直接求
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i,j = 0,0
        while candies > 0:
            if candies - i - j - 1 >= 0:
                result[i] = result[i] + i + j + 1
            else:
                result[i] = result[i] + candies
            candies = candies - i - j - 1
            i = (i + 1) % num_people
            if i == 0:
                j = j + num_people
        return result