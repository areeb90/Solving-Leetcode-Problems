class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            largest_sum = max(largest_sum, curr_sum)
            
        return largest_sum