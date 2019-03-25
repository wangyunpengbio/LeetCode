class Solution:
    def intToRoman(self, num: int) -> str:
        valuelist = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        replist = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ""
        for i in range(13):
            while(num>=valuelist[i]):
                num = num - valuelist[i]
                res = res + replist[i]
        return res