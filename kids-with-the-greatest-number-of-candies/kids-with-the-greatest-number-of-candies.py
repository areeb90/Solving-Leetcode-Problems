class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		maxValue = max(candies)
		Out = []
		for i in range(len(candies)):
			if candies[i] + extraCandies >= maxValue:
				Out.append(True)
			else:
				Out.append(False)

		return Out