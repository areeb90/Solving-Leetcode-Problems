class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1
        minValue = nums[0]+1
        for i in range(len(nums)):
            if nums[i] > minValue:
                diff = max(diff, nums[i]- minValue)
            
            minValue = min(minValue, nums[i])                   #assigns the minimun value on every iteration
            
        return diff