class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # map(bool, nums) ______ this is TRUE every time in all ZEROES condition 
        
        if not any(map(bool, nums)):
        # if not any(map(bool, nums))________ and this means there is no TRUTH VALUE PRESENT in this array
            return "0"
        
        
        
        # converts all integer values as strings in this array, and will be treated as Strings
        nums = list(map(str, nums))
        
        def compare(x , y):
            return int(nums[x] + nums[y]) > int(nums[y] + nums[x])
        
        
        for x in range(len(nums)-1):
            y = x + 1
            while (x < len(nums)-1) and (y < len(nums)):
                if compare(x,y):
                    pass
                else:
                    nums[x], nums[y] = nums[y] , nums[x]
                
                y+=1
        return "".join(nums)
            
        