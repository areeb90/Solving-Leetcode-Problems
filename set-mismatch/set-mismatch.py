class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0)+1
            
            
        duplicate =  missing = 0
        for i in range(1 , len(nums)+1):
            if i not in dic:
                missing = i
            elif dic[i] == 2:
                duplicate = i
            
            if missing and duplicate :
                return [duplicate , missing]
        
        
        
        
        
        
#         res = []
#         non_d = []
#         for i in range(len(nums)):
            
#             if nums[i] in non_d:
#                 res.append(nums[i])
#             else:
#                 non_d.append(nums[i])
                
#         for i in range(1, len(nums)+1):
#             if i not in nums:
#                 res.append(i)
                
#                 return res

                
                # result = [duplicate , miss]