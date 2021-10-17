class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count=1
        sett = set(nums)
        while count:
            if count not in sett:
                return count
            count +=1
            
        
        
#         for i in range(1, len(nums)+1):
#             if i not in nums:
#                 return i
#             elif len(nums) <2:
#                 return 2
            