class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         dic={}
#         for n in nums:
#             if n not in dic:
#                 dic[n]=1
#             else:
#                 dic[n] +=1
            
#             if dic[n] > (len(nums)/2):
#                 return n
            
#       time complexity = O(n)
#       space complexity = O(1)
            
        
            nums = sorted(nums)
            midIndex=len(nums)//2
            return nums[midIndex]