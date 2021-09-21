class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         lPointer , rPointer = 0 , len(nums)-1
        
#         while rPointer > lPointer:
#             currentSum = nums[lPointer] + nums[rPointer]
#             if currentSum > target :
#                 rPointer -= 1
#             elif currentSum < target:
#                 lPointer +=1
#             else:
#                 return [lPointer  , rPointer]
            
#         return []
            
    
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                curSum = nums[i]+nums[j]
                if curSum == target:
                    return [i , j]
                

    
        
    
    
a = Solution()
a.twoSum([2,3,4,8,4,7,5,1], 12)

