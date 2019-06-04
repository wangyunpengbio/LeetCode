class Solution:
    # 没考虑重复点，重复点会出错，其他都可以通过
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==0:return 0
        points = list(set(tuple(item) for item in points))
        from collections import defaultdict
        dic = defaultdict(set) # 存储: 键key为斜率k，值value为可以计算出该斜率的两点坐标
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                if points[i][0] - points[j][0] == 0:
                    k = float("inf")
                else:
                    k = (points[i][1] - points[j][1])/(points[i][0] - points[j][0])
                dic[k].add((tuple(points[i]),tuple(points[j])))
        # print(dic)
        dicY = defaultdict(list) # 存储: 键key为斜率k，值value为与Y轴相交的坐标
        for k,v in dic.items():
            for value in v:
                pointsA,pointsB = value
                if pointsA[0] - pointsB[0] == 0:
                    Y = float("inf")
                else:
                    Y = (pointsA[0]*pointsB[1] - pointsB[0]*pointsA[1])/(pointsA[0] - pointsB[0])
                dicY[k].append(Y)
        # print(dicY)
        maxNum = 0
        dicRes = {}
        for k,v in dicY.items():
            for value in v:
                dicRes.setdefault((k,value), 0)
                dicRes[(k,value)] += 1
            maxNum = max(maxNum,dicRes[(k,value)])
        # print(dicRes)
        num = (1+(1+8*maxNum)**0.5)/2
        return int(num)