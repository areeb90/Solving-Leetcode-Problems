class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for index, value in enumerate(nums):
            if (index != value):
                return index
        return len(nums)