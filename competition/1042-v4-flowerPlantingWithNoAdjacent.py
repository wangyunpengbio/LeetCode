class Solution:
    def gardenNoAdj(self, N, paths):
        # 与i相连的公园的flower找到,填充不一样flower 就行了
        from collections import defaultdict
        res = [0] * N
        graph = defaultdict(set)
        for path in paths:
            graph[path[0]].add(path[1])
            graph[path[1]].add(path[0])

        def connected_grade(i):
            ans = []
            for g in graph[i]: # 遍历与i相连的公园
                # print(g)
                if res[g - 1] != 0: # 如果与i相连的公园的flower种过了，不为0，追加到ans中
                    ans.append(res[g - 1])
            return ans   # 找到与i相连的公园种的flower

        for i in range(1, N + 1):
            tmp = connected_grade(i)
            # print(tmp)
            flower = 1
            while flower in tmp: # 如果该flower已经在相邻花园被种过，就换一种花，直到没种过
                flower += 1
            res[i - 1] = flower  # 当前garden种花
        return res