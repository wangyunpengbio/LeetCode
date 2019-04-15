class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """ 
        就是依次1、2、3乘以5，再1、2、3乘以4
        num1的第i位(高位从0开始)和num2的第j位相乘的结果在乘积中的位置是[i+j]和[i+j+1]
        例: 123 * 45,  123的第1位 2 和45的第0位 4 乘积 08 存放在结果的第[1] 和[2]位中
          index:    0 1 2 3 4  
              
                        1 2 3
                    *     4 5
                    ---------
                          1 5  --3*5
                        1 0    --2*5
                      0 5      --1*5
                    ---------
                      0 6 1 5
                        1 2    --3*4
                      0 8      --2*4
                    0 4        --1*4
                    ---------
                    0 5 5 3 5
        这样我们就可以单独都对每一位进行相乘计算把结果存入相应的index中"""
        num1_len = len(num1)
        num2_len = len(num2)
        res = [0] * (num1_len + num2_len)
        for i in range(num1_len-1,-1,-1):
            for j in range(num2_len-1,-1,-1):
                tmp = int(num1[i]) * int(num2[j]) + int(res[i+j+1])
                res[i+j+1] = tmp%10
                res[i+j] = res[i+j] + tmp//10
                # print(res)
        res = list(map(str, res))
        # print(res)
        for i in range(num1_len+num2_len):
            print(i)
            if res[i]!='0':
                return ''.join(res[i:])
        return '0'
            