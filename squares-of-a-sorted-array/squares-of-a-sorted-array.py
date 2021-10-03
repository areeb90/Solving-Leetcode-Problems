class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            sq = i*i
            arr.append(sq)
        return sorted(arr)