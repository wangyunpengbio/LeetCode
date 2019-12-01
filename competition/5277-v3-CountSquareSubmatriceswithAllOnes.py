class Solution:
    # 把java的代码重新实现了一遍，超时
    def countSquares(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix),len(matrix[0])
        length = min(row,col)
        dp = [[[False for k in range(length)] for j in range(col)] for i in range(row)]
        num = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    dp[i][j][0] = True
                    num += 1
        for i in range(1,row):
            for j in range(1,col):
                for k in range(1,length):
                    dp[i][j][k] = matrix[i][j] == 1 and dp[i - 1][j][k - 1] and dp[i][j - 1][k - 1] and dp[i - 1][j - 1] [k - 1]
                    if dp[i][j][k]:
                        num += 1
        return num
# 设dp[i][j][k]表示以(i, j)为右下角，边长为k的正方形区域是否全为1，那么易得出如下状态转移方程：
# dp[i][j][k] = (matrix[i][j] == 1 && dp[i - 1][j][k - 1] && dp[i][j - 1][k - 1] && dp[i - 1][j - 1] [k - 1]);

# class Solution {
#     public int countSquares(int[][] matrix) {
#         int m = matrix.length;
#         int n = matrix[0].length;
#         int len = Math.min(m, n);
#         boolean[][][] dp = new boolean[m][n][len];
#         int count = 0;
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 dp[i][j][0] = (matrix[i][j] == 1);
#                 count += dp[i][j][0] ? 1 : 0;
#             }
#         }
#         for (int i = 1; i < m; i++) {
#             for (int j = 1; j < n; j++) {
#                 for (int k = 1; k < len; k++) {
#                     dp[i][j][k] = (matrix[i][j] == 1 && dp[i - 1][j][k - 1] && dp[i][j - 1][k - 1] && dp[i - 1][j - 1] [k - 1]);
#                     if (dp[i][j][k]) {
#                         count++;
#                     }
#                 }
#             }
#         }
#         return count;
#     }

# }

# 作者：97wgl
# 链接：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/tong-ji-quan-wei-1-de-zheng-fang-xing-zi-ju-zhen-f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。