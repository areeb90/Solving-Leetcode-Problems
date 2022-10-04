class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueElement = set()
        for i in nums:
            if i in uniqueElement:
                return True
            else:
                uniqueElement.add(i)
        return False
        
        
        
        # uniqueElement = set(nums)
        # count=0
        # for i in nums:
        #     if i in uniqueElement:
        #         count+=1
        #     else:
        #         count+=1
        # if count>=2:
        #     return True
        # else:
        #     return False
        
        
        # l = []
        # for i in nums:
        #     if i not in l:
        #         l.append(i)
        #     else:
        #         return True
        # return False
        
        
        
        # l=[]
        # count=0
        # for i in nums:
        #     if i in l:
        #         count+=1
        #     else:
        #         l.append(i)
        #         count+=1
        # if count>=2:
        #     return True
        # else:
        #     return False