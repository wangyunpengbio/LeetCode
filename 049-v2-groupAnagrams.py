class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        # 作为键的字符串不用再遍历，改为一串数组进行存储
        # 如abbccc表示为(1,2,3,0,0，...，0)，共有26个条目
        # 如bbcdd表示为(0,2,1,2,0，...，0)，共有26个条目
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()