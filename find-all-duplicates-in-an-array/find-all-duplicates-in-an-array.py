class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        res = []
        
        for i,j in c.items():       #i holds all the items in an array , while  j tracks tha how many copies of                                     each item is present in an array 
            if j == 2:
                res.append(i)
        return res
        
        # res = []
        # for i in nums:
        #     if nums.count(i) >1 and i not in res:
        #         res.append(i)
        # return res
        
        