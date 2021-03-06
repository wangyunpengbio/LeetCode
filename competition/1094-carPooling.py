class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort()
        dicUp = {} # 位置->上车人数
        dicDown = {}
        for trip in trips:
            if dicUp.get(trip[1]):
                dicUp[trip[1]] = trip[0] + dicUp[trip[1]]
            else:
                dicUp[trip[1]] = trip[0]
            if dicDown.get(trip[2]):
                dicDown[trip[2]] = trip[0] + dicDown[trip[2]]
            else:
                dicDown[trip[2]] = trip[0]
        cur = 0
        for pos in range(1000): # 题目中规定了最远距离是1000 0 <= trips[i][1] < trips[i][2] <= 1000
            if dicDown.get(pos):
                cur = cur - dicDown.get(pos)
            if dicUp.get(pos):
                cur = cur + dicUp.get(pos)
            if cur > capacity:
                return False
        return True