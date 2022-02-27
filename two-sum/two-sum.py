class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        nums_dict = {}
        for i in range(len(nums)):
            cur_num = nums[i]
            nums_dict[cur_num] = i
            
        for i in range(len(nums)):
            cur_num = nums[i]
            check_num = target - cur_num
            if check_num in nums_dict:
                if nums_dict[check_num] != i:
                    return(i , nums_dict[check_num])
            
            
    
#         for i in range(0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 curSum = nums[i]+nums[j]
#                 if curSum == target:
#                     return [i , j]
                

    
a = Solution()
a.twoSum([2,3,4,8,4,7,5,1], 12)

