class Solution:
    # 深度优先遍历 超时
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s,wordDict):
            if len(s)==0: # 剩余长度为0 则正好分割完
                return True
            else:
                for item in wordDict:
                    N = len(item)
                    if len(s) < N:continue
                    if s[:N] == item:
                        if dfs(s[N:],wordDict):
                            return True
                return False
        return dfs(s,wordDict)