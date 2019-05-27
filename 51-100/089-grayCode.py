class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 格雷编码与二进制 https://wenku.baidu.com/view/340671ef69dc5022abea005e.html
        # 博客说明 https://blog.csdn.net/w8253497062015/article/details/80896500
        size = 1 << n
        res = []
        for i in range(size):
            graycode = i ^ (i>>1)
            res.append(graycode)
        # print([bin(item) for item in res]) 
        return res
