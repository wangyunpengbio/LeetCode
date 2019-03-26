# 超出时间限制
class Solution:
    # 将三数之和转化为两数之和
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = set()
        for item in nums:
            other = target - item
            if other in hashmap:
                yield [other,item]
            hashmap.add(item)
        return None
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        resSet = []
        # 少于三个数字自动返回空列表,虽然测试用例的程序是可以多次使用同一个数字，意味着输入[0,0]也应该返回[0,0,0]，但是此种方式测试用例并不认可
        if len(nums) < 3: return res
        # 为了去除重复，同步维护一个[{},{},{}]的列表进行去重复
        for i in range(0,len(nums)):
            others = nums[:i]
            others.extend(nums[i+1:])
            # 由于同一个数字也可能由列表中不同组合生成，此处使用生成器
            sublistGen = self.twoSum(others, -nums[i])
            for sublist in sublistGen:  
                sublist.append(nums[i])
                subset = set(sublist)
                if subset not in resSet:
                    res.append(sublist)
                    resSet.append(subset)
        return res