class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearchh(nums, target , True)
        right = self.binSearchh(nums, target , False)
        return [left, right]
    def binSearchh(self , nums, target, leftBias):
        l , r = 0 , len(nums)-1
        i = -1
        while (l <= r):
            mid=(l+r)//2
            if nums[mid]< target:
                l = mid +1
            elif nums[mid] > target:
                r= mid-1
            else:
                i = mid
                if leftBias:
                    r = mid-1
                else:
                    l = mid+1
        return i
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not nums:
#             return [-1, -1]
#         start, end = -1,-1
#         N = len(nums)
#         l , r = 0 , N
#         #for left search
#         while (l < r):
#             mid = (l + r)//2
#             if nums[mid] >= target:
#                 r = mid
#             else:
#                 l = mid+1
#         if (l<r) and (nums[l] == target):
#                 start = l
                
#         #for right search
#         l , r = 0 , N
#         while (l < r):
#             mid = (l+r)//2
#             if nums[mid]<= target:
#                 l = mid+1
#             else:
#                 r = mid
#         if nums[r-1] == target:
#                 end = r-1
                
#         return [start , end]