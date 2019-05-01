class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for itlist in matrix:
            # 直接逐行比较是否存在
            if target in itlist:
                return True
            # 如果目标比当前行最小的还要小，则不会再找到
            try: # 异常处理 [[]] 这样的空列表特例
                if target < itlist[0]:
                    break
            except:
                pass
        return False