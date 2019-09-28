class Solution:
    # 依旧超时，但是通过更多的样例
    # result二维数组动态规划，result[i][j]表示从i到j位运算结果
    def subarrayBitwiseORs(self, A) -> int:
        countSet = set()
        result = [[False] * len(A) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(i,len(A)):
                if i == j:
                    result[i][j] = A[i]
                else:
                    result[i][j] = result[i][j - 1] | A[j]
                countSet.add(result[i][j])
        return len(countSet)

class Solution:
    # 比上面优化了set数组，变成list，不用每次添加元素都去重复
    # result二维数组动态规划，result[i][j]表示从i到j位运算结果
    def subarrayBitwiseORs(self, A) -> int:
        countSet = []
        result = [[False] * len(A) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(i,len(A)):
                if i == j:
                    result[i][j] = A[i]
                else:
                    result[i][j] = result[i][j - 1] | A[j]
                countSet.append(result[i][j])
        return len(set(countSet))