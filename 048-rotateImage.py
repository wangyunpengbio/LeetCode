class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先转最外面的那圈，从外到内一圈一圈转
        for k in range(n//2): # 5*5矩阵只用转外面的4圈就可以了
            # print(k)
            # i表示当前跳到的位置，要跳n-2*k-1次(-1是因为最后一个元素不用跳)
            for i in range(n-2*k-1):
                # print((k,i+k),(n-k-i-1,k),(n-k-1,n-k-i-1),(k+i,n-k-1))
                # if i == n//2:continue # 如果是奇数的方阵,正中间的元素不用转，改行不能加，因为加了以后偶数方正中间会跳过
                tmp = matrix[k][i+k]
                matrix[k][i+k] = matrix[n-k-i-1][k]
                matrix[n-k-i-1][k] = matrix[n-k-1][n-k-i-1]
                matrix[n-k-1][n-k-i-1] = matrix[k+i][n-k-1]
                matrix[k+i][n-k-1] = tmp