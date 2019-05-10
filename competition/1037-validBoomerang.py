class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 先比较是否为同一个点
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                if points[i] == points[j]:
                    return False
        # 再比较横坐标是否相同
        if points[0][1] == points[1][1] and points[0][1] == points[2][1]:
            return False
        elif points[0][1] != points[1][1] and points[0][1] == points[2][1]:
            return True
        elif points[0][1] == points[1][1] and points[0][1] != points[2][1]:
            return True
        # 最后计算斜率
        k1 = (points[0][0]-points[1][0])/(points[0][1]-points[1][1])
        k2 = (points[0][0]-points[2][0])/(points[0][1]-points[2][1])
        if k1 == k2:
            return False
        else:
            return True