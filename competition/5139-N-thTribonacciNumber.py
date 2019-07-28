class Solution:
    # 每次只算三个数字
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]
        if n <= 2:
            return arr[n]
        else:
            for i in range(3,n+1):
                arr[i%3] = sum(arr)
            return arr[i%3]