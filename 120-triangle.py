class Solution:
    # 超出时间限制
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(minRoute,curRoute,index,triangle,level):
            if level == len(triangle):
                # print(curRoute)
                minRoute[0] = min(minRoute[0],curRoute)
                return None
            else:
                dfs(minRoute,curRoute+triangle[level][index],index,triangle,level+1)
                dfs(minRoute,curRoute+triangle[level][index],index+1,triangle,level+1)
        minRoute = [float("inf")]
        dfs(minRoute,0,0,triangle,0)
        return minRoute[0]