class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 动态规划递推公式: 当前位置最长匹配长度 = 当前匹配长度 + 上一个位置的最长匹配长度
        
        # // f[i]表示以i结尾的有效的括号的长度
        # // )必须在前面找一个(,即i-1-f[i-1]
        # // 若匹配上了,还要加上再前面的哪一个串
        
        #length_effec[i]表示以i结尾的有效括号的长度
        #动态规划代码如下：
        #其中如果s[i]=='('令length_effec[i]为0；
        # 如果s[i]==')'时，则去寻找它的一个匹配'(',
        #(假如以s[i-1]结尾的字符串存在有效括号串，那么与s[i]匹配的括号一定不出现在length_effect[i-1]范围内)
        # 因此需要跳出length_effect[i-1]的范围，即查看s[i-length_effect[i-1]-1]的值是否等于'('，
        # 

        #初版，有一些地方还不成熟
        # s_len = len(s)
        # if s_len==0:
        #     return 0
        # length_effect = [0 for i in range(s_len)]
        # for i in range(1, s_len):
        #     if s[i] == ')':
        #         if s[i - 1] == '(':
        #             if i - 2 >= 0:
        #                 length_effect[i] = length_effect[i - 2] + 2
        #             else:
        #                 length_effect[i] = 2
        #         else:
        #             if s[i - length_effect[i - 1] -
        #                  1] == '(' and i - length_effect[i - 1] - 1 >= 0:
        #                 length_effect[i] = length_effect[i - 1] + 2+length_effect[i - length_effect[i - 1] - 1 -1]
        # print(length_effect)
        # return max(length_effect)

        #终版
        s_len = len(s)
        if s_len == 0:
            return 0
        length_effect = [0 for i in range(s_len)]
        for i in range(1, s_len):
            if s[i] == ')':
                #如果越界则表示不匹配，直接令对应的length_effect位置为0
                if i - length_effect[i - 1] - 1 >= 0 and s[i - length_effect[i - 1] - 1] == '(':
                    length_effect[i] = length_effect[i - 1] + 2
                #对越界情况进行检查，越界表示前面不存在，就不需要进行求和
                if i - length_effect[i] >= 0:
                    length_effect[i] += length_effect[i - length_effect[i]]
            print(length_effect)
        return max(length_effect)