class Solution:
    # 数组从后往前计算分数值即可，每次计算之后互换分子和分母并约分。
    # 在草稿纸上写清楚过程
    def fraction(self, cont):
        cont.insert(-1,1)
        while len(cont) > 2:
            # print(cont)
            tmp = cont[-3] * cont[-1] + cont[-2]
            left = cont[-1]
            cont.pop(-1)
            cont.pop(-1)
            cont.pop(-1)
            cont.append(left)
            cont.append(tmp)
        return [cont[1],cont[0]]