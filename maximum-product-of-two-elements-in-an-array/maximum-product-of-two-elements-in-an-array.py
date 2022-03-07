class Solution:
    def maxProduct(self, nums: List[int]) -> int:
#         max_prod = 0
#         for i in range(len(nums)):
#             for j in range(i , len(nums)):
#                 if i!= j:
#                     max_i_j = (nums[i]-1) * (nums[j]-1)
                
#                     if max_i_j > max_prod:
#                         max_prod = max_i_j
                
#         return max_prod



#     time complexity => O(n^2)
#     space complexity => O(1)

    
    
#         nums = sorted(nums)
#         num1 = nums[-1]
#         num2 = nums[-2]
#         return (num1-1)*(num2-1)
    
#     time complexity => O(nlogn)
#     space complexity => O(1)




        num1 = 0
        for i in range(len(nums)):
            if nums[i]>num1:
                num1 = nums[i]
            
        nums.remove(num1)
        
        num2 = 0
        for i in range(len(nums)):
            if nums[i]>num2:
                num2=nums[i]
        nums.remove(num2)
        
        return (num1-1)*(num2-1)

#     time complexity => O(n)
#     space complexity => O(1)

#     time complexity => O(n^2)
#     space complexity => O(1)
