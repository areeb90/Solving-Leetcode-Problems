class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}   # Stores the first position of each number
        last = {}    # Stores the last position of each number


        # Step 1: Fill first and last dictionaries
        for index, value in enumerate(nums):
            first.setdefault(value, index)   # Only set if not already in the dictionary
            last[value] = index              # Always update to the latest position


        # Step 2: Count how many times each number appears

        count = Counter(nums)               
        degree = max(count.values())     # Find the maximum frequency (degree)


        # Step 3: Find the shortest subarray with the same degree

        min_length = float('inf')       # Start with infinity for comparison
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1    
                min_length = min(min_length, length)  # Update the minimum length
            
        return min_length