# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    class Meta:
        def __init__(self, point=0, mark=""):
            self.point = point
            self.mark = mark
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        res = []
        final = []
        allpoint = []
        rightpoint = []
        flag = True # flag表示是否重叠
        # 把两者可能重叠的区间追加到allpoint中
        for i,item in enumerate(intervals):
            # 左侧没重叠部分先弄到结果的list中
            if item[1] >= newInterval[0]: # 如果该条件满足，则开始重叠
                flag = False
            if  flag: # 开始重叠就不把元素放到结果的list中了
                final.append(item)
            # 右侧没重叠部分最后直接弄到中间暂存的rightpoint中
            if item[0] > newInterval[1]:
                rightpoint.extend(intervals[i:])
                break
            # 重叠部分放到allpoint中进行后续重叠计算
            if not flag:
                allpoint.append(self.Meta(item[0],"->"))
                allpoint.append(self.Meta(item[1],"<-"))
        # print(final,rightpoint)
        # 加入新的那个区间
        allpoint.append(self.Meta(newInterval[0],"->"))
        allpoint.append(self.Meta(newInterval[1],"<-"))
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
        final.extend(rightpoint)
        return final