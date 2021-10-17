class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        targetList = []
        targetList.append(nums[0])
        for i in range(1,len(nums)):
            targetList.insert(index[i] , nums[i])
        return targetList
        
    