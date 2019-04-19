# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # 自定义一个数据结构 point为数据点的位置 mark为数据点的方向"->"表示有效区间向右，"<-"表示有效区间向左
    class Meta:
        def __init__(self, point=0, mark=""):
            self.point = point
            self.mark = mark
    def merge(self, intervals):
        res = []
        final = []
        allpoint = []
        for item in intervals:
            allpoint.append(self.Meta(item[0],"->"))
            allpoint.append(self.Meta(item[1],"<-"))
        allpoint.sort(key=lambda p:p.point)
        # tmplist为栈结构，将重叠部分合并
        tmplist = []
        for i,item in enumerate(allpoint):
            tmplist.append(item.point)
            if item.mark == "<-":
                tmplist.pop()
                tmp = tmplist.pop()
            if len(tmplist) == 0:
                start = tmp
                end = item.point
                res.append([start,end])
            # print(item.point,item.mark)
        # print(res)
        while res:
            current = res.pop(0)
            while res: # 如果是[1, 5], [5, 10]，则直接变成[1, 10]，去除掉连接点
                tmp = res.pop(0)
                if tmp[0]==current[1]:
                    current[1] = tmp[1]
                else:
                    res.insert(0,tmp)
                    break
            # print(current)
            final.append(current)
        return final
