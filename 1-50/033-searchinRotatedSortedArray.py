class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 参考 https://zhuanlan.zhihu.com/p/64841956 其中的思路二
        if len(nums) == 0:
            return -1
        head = 0
        tail = len(nums)-1
        while head < tail:
            # print(head,tail)
            if target>nums[tail] and target<nums[head]: # 找不到
                return -1
            else:
                middle = int((head+tail)/2)
                if nums[middle] == target: # 找到了
                    return middle
                elif nums[middle] >= nums[head]: # 左边有序 # 此处的等号要多试几次才行
                    if nums[head] <= target < nums[middle]: # 在左边
                        tail = middle - 1
                    else:                                   # 在右边
                        head = middle + 1
                else: # 右边有序
                    if nums[middle] < target <= nums[tail]: # 在右边
                        head = middle + 1
                    else:                                   # 在左边
                        tail = middle - 1
        # print(head,tail)
        if nums[head] == target:
            return head
        elif nums[tail] == target:
            return tail
        else:
            return -1
