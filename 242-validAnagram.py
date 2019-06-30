class Solution:
    # 哈希表，记录每个字母在s中出现的次数，然后减去在t中出现的次数，出现非零则为False
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dic = defaultdict(int)
        for item in s:
            dic[item] = dic[item] + 1
        for item in t:
            dic[item] = dic[item] - 1
        for value in dic.values():
            if value != 0:
                return False
        return True