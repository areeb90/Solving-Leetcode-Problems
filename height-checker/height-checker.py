class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedH = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sortedH[i] != heights[i]:
                count +=1
            else:
                pass
        return count