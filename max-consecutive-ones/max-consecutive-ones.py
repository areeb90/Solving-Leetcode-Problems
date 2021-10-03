class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        c=[]
        for i in range (len(nums)):
            if nums[i]==1:
                count +=1 
                
            else:
                count = 0
            c.append(count)
        return max(c)
            
            