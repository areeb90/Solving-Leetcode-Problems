class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            sq = i*i
            l.append(sq)
        return sorted(l)