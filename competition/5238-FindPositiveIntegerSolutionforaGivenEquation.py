"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    # 直接挨个遍历即可，由于是单调递增，如果复杂度高可以用二分查找
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        resultlist = []
        for i in range(1,1001):
            for j in range(1,1001):
                if customfunction.f(i,j) == z:
                    resultlist.append([i,j])
                elif customfunction.f(i,j) > z:
                    break
        return resultlist