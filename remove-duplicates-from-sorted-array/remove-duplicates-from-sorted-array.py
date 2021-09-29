class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        current= nums[0]                
        index = 1                       #Unique first number           --[0]th index
        for i in nums[1:]:                 
            if i>current:
                current = i
                nums[index] = current
                index +=1

        return index