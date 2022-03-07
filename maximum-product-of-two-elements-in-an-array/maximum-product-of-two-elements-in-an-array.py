class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 0
        for i in range(len(nums)):
            for j in range(i , len(nums)):
                if i!= j:
                    max_i_j = (nums[i]-1) * (nums[j]-1)
                
                    if max_i_j > max_prod:
                        max_prod = max_i_j
                
        return max_prod
            