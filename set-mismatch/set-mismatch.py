class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result=[]
        Set = []
        for i in range(len(nums)):
            if nums[i] in Set:
                result.append(nums[i])
            else:
                Set.append(nums[i])
        
        for i in range(1, len(nums)+1):
            if i not in nums:
                result.append(i)
                return result
            