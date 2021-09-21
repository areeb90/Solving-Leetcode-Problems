class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffledArray = []
        for i in range(n):
            shuffledArray.extend([nums[i], nums[i+n]])
            
        return shuffledArray 
