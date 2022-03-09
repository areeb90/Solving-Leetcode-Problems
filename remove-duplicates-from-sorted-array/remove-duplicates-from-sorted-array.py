class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        ctrl_pointer=1
        for i in range(1, len(nums)):
            if (nums[i] != nums[i-1]):
                nums[ctrl_pointer]=nums[i]
                ctrl_pointer+=1
        return ctrl_pointer        
        
        
        # if len(nums)==0:
        #     return 0
        # current = nums[0]
        # index = 1              #Unique first number           --[0]th index
        # for i in nums[1:]:
        #     if i> current:
        #         current = i
        #         nums[index] = current
        #         index +=1
        # return index
    
    
