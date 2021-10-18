class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for i in nums:
            if i in sett:
                return True
            
            else:
                sett.add(i)
                
        return False