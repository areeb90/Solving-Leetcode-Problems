class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.           
        """
        k = k % len(nums)
                                                    #[1,2,3,4,5,6,7]  k = 3
        
        l , r = 0 , len(nums)-1                     #just swap the first element with the last one  [7,6,5,    4,3,2,1]
        while l < r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l , r = l+1 , r-1
            
            
        l , r = 0 , k-1                             #swap the element (first with last) in the ___k___ range  [5,6,7]
        while l < r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l , r = l+1 , r-1
        
        
        l , r = k , len(nums)-1                     #swapping items of the remaining part   [1,2,3,4]
        while l < r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l , r = l+1 , r-1                       #final array becomes   [5,6,7,1,2,3,4]
            