class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Sum = 0
        return [Sum := Sum + x for x in nums]