class Solution:
    # 深度优先遍历，找出所有可能性，最后去掉空字符串的那个
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(results,res,tiles):
            results.add(res)
            for i in range(len(tiles)):
                dfs(results,res+tiles[i],tiles[:i]+tiles[i+1:])
        results = set()
        dfs(results,"",tiles)
        return len(results) - 1