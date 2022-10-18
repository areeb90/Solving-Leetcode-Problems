class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        l, r = 0 , len(nums)-1
        
        while l<=r:
            if nums[l] * nums[l] > nums[r]*nums[r]:
                arr.append(nums[l]*nums[l])
                l = l+1
                
            else:
                arr.append(nums[r]*nums[r])
                r-=1
        return arr[::-1]
        
        
        
        # for i in nums:
        #     sq = i*i
        #     l.append(sq)
        # return sorted(l)