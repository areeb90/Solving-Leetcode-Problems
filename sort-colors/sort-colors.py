class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #red , white = 0 | blue = 2
        #red == low | white == i | blue == high
        
        low = 0
        i = 0
        high = len(nums)-1
        while (i <= high):
            if (nums[i] == 0):
                nums[i], nums[low] = nums[low] , nums[i]
                low+=1
                i+=1
            elif (nums[i]==2):
                nums[high] , nums[i] = nums[i] , nums[high]
                high -=1
                
            else:
                i+=1