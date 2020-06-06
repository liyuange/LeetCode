from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return {dict[target-x], i}
            else:
                dict[x] = i
