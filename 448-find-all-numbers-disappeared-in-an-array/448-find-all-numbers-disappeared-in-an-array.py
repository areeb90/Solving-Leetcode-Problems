class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        temp = set(nums)
        for i in range(1, len(nums)+1):
            if i not in temp:
                res.append(i)
        return res
