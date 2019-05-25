class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 深度优先遍历
        def dfs(results,result,s,level):
            # print(results,s)
            if len(s) == 0 and level == 4:
                results.add(".".join(result))
                return None
            if level >= 4: # 超出4段ip的话就跳过
                return None
            for i in range(1,4):# 每个ip地址最多三位数字
                if s[:i] != "" and 0 <= int(s[:i]) <= 255: # 保证每段ip不为空 且在0-255
                    if len(s[:i]) >= 2 and s[0] == "0":continue # 保证每段ip没有 01.011.010这样的
                    dfs(results,result + [s[:i]],s[i:],level + 1)
        results = set()
        dfs(results,[],s,0)
        return list(results)