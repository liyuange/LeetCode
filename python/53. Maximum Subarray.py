class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curr_max_sum = max_sum = nums[0]
        for i in range(1, n):
            curr_max_sum = max(curr_max_sum + nums[i], nums[i])
            max_sum = max(curr_max_sum, max_sum)
        return max_sum

