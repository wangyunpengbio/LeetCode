class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort()
        dicUp = {} # 位置->上车人数
        dicDown = {}
        for trip in trips:
            dicUp[trip[1]] = dicUp.setdefault(trip[1], 0) + trip[0]
            dicDown[trip[2]] = dicDown.setdefault(trip[2], 0) + trip[0]
        cur = 0
        for pos in range(1000): # 题目中规定了最远距离是1000 0 <= trips[i][1] < trips[i][2] <= 1000
            if dicDown.get(pos):
                cur = cur - dicDown.get(pos)
            if dicUp.get(pos):
                cur = cur + dicUp.get(pos)
            if cur > capacity:
                return False
        return True