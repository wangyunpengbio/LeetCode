class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 将字符串排序后转化为元组当做字典的键(字典的键只能由元组和字符串这样的不可变元素构成，列表这样可变元素不可以当做键)
        ans = {}
        for item in strs:
            key = tuple(sorted(item))
            ans.setdefault(key,[]).append(item)
        return list(ans.values())
        # 官方解答：collections.defaultdict用来保证加入新字符的时候直接返回空列表以供追加
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return list(ans.values())