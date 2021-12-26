class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j=1
        for i in range(1, n):
            if (nums[i] != nums[i-1]):
                nums[j]=nums[i]
                j+=1
        return j        
        
        
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
    
    
