class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        res = set() # 集合去除重复
        dic = {}
        for i in range(len(s)-9): # 从头到尾，末尾是-9
            dic[s[i:i+10]] = dic.setdefault(s[i:i+10],0) + 1
        # print(dic)
        for key,value in dic.items():
            if value >= 2:
                res.add(key)
        return list(res)