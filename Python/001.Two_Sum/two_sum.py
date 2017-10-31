class Solution(object):
    def twoSum(self, nums, target):
        # 方法1
        for i, num in enumerate(nums):
            temp_nums = nums[i+1:]
            if target - num in temp_nums:
                return [i, temp_nums.index(target-num)+i+1]

    def twoSum2(self, nums, target):
        # 方法2
        avg = target / 2 + target % 2

        while True:
            if avg in nums:
                index1 = nums.index(avg)
                nums[index1] = 'x'
                if (target - avg) in nums:
                    index2 = nums.index(target - avg)
                    return [index1, index2]
                nums[index1] = avg
            avg -= 1
