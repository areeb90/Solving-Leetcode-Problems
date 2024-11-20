class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num)-1 
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [index + 1 for index in range(len(nums)) if nums[index] > 0]