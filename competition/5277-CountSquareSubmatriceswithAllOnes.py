class Solution:
    # 该思路是错的，这个思路就是先找最大的正方形，然后整个mask成0，再依次找剩下来的较小正方形（但是这样mask完了以后，计数会变少）
    def countSquares(self, matrix: List[List[int]]) -> int:
        def len2Num(i):# 计算该长度的正方形包括多少子正方形
            num = 0
            for i in range(1,i+1):
                num = num + i ** 2
            return num
        def testSubMatrix(matrix,startRow,startCol,endRow,endCol):# 检测当前“子区域”是否全为1
            sumNum = 0
            for i in range(startRow,endRow):
                sumNum += sum(matrix[i][startCol:endCol])
            if sumNum == (endRow - startRow) * (endCol - startCol):
                return True
            else:
                return False
        def showmatrix(matrix):
            for item in matrix:
                print(item)
            print("----------")
        num = 0
        for startRow in range(len(matrix)):
            for startCol in range(len(matrix[0])):
                for length in range(300,0,-1):
                    if startRow+length > len(matrix) or startCol+length > len(matrix[0]):
                        continue
                    if testSubMatrix(matrix,startRow,startCol,startRow+length,startCol+length):
                        num += len2Num(length)
                        for i in range(startRow,startRow+length):
                            for j in range(startCol,startCol+length):
                                matrix[i][j] = 0
                        print(num)
                        showmatrix(matrix)
        return num
                        
