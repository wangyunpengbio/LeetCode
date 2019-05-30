class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 使用哈希表记录每个数字出现的次数
        dd = {}
        for item in nums:
            dd.setdefault(item, 0)
            dd[item] = dd[item] + 1
        # print(dd)
        for key,value in dd.items():
            # print(key,value)
            if value == 1:
                return key