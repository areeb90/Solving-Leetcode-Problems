class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett= set()
        for i in nums:
            if i in sett:
                return i
            else:
                sett.add(i)