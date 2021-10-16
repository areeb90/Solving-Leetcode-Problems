class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = list(set(nums))
        l = sorted(l)
        if len(l) >=3:
            return l[-3]
        else:
            return l[-1]
        
        
        
        
        
#         l = []
#         if len(nums) <3:
#             return 0
#         for i in nums:
#             if i not in l:
#                 l.append(i)
#             else:
#                 pass
        
#         l = sorted(l)
#         return l[-3]

    
            