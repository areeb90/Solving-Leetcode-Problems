class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k =0 
        
#         val-- not to be included in an array, while others elements are included in a sequence
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
                
        return k  #returning the length of the sequence