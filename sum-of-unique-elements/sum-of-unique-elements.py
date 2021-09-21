class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # unique = []
        # sum=0
        # for x in nums:
        #     if nums.count(x)==1:
        #         sum +=x
        # return sum
        
        l=[]
        summ=0
        for i in nums:
           if nums.count(i)==1:
            l.append(i)
        for j in l:
            summ +=j

        return summ
        