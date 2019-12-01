class Solution:
    # 直接用二元一次方程求出解
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        numJumbo,test1 = divmod((tomatoSlices - 2 * cheeseSlices),2)
        numSmall,test2 = divmod((4 * cheeseSlices - tomatoSlices),2)
        if test1 != 0 or test2 != 0 or numJumbo < 0 or numSmall < 0:
            return []
        else:
            return [numJumbo,numSmall]
