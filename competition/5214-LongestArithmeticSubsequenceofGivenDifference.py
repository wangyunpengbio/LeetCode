class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # 如果间距为0，则直接统计出现最多的元素即可
        if difference == 0:
            from collections import Counter
            count = Counter(arr)
            return count.most_common(1)[0][1] # 最多元素出现的次数
        # 间距不为0，把下一个需要的元素当做键，这一串已经出现过的数字放入set集合中，最后统计最长的set集合即可
        from collections import defaultdict
        dic = defaultdict(set)
        for index,item in enumerate(arr):
            if item not in dic:
                dic[item + difference].add(item)
            else:
                # 改键，再追加当前元素
                dic[item + difference] = dic.pop(item)
                dic[item + difference].add(item)
        maxLen = 0
        for value in dic.values():
            maxLen = max(maxLen,len(value))
        return(maxLen)

'''
dp[i] 代表以 i 为结尾时，子序列能形成的最大长度。
例如, 当前 diff 为 2, 且当前遍历到了 5, 此时 5 最多可以和之前的 3(5-2) 连到一起,
去查找之前以 3 为结尾的最大值 + 1 和 以 5 为结尾的最大值进行比较，然后比较一下即可。

C++
    int longestSubsequence(vector<int>& arr, int diff) {
        int res = 1;
        unordered_map<int, int> has;
        for(auto it : arr) {
            has[it] = max(has[it], has[it - diff] + 1);
            res = max(res, has[it]);
        }
        return res;
    }

作者：Lingo
链接：https://leetcode-cn.com/circle/discuss/x0KbRs/view/n2Xbup/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''