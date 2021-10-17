class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death , -1))
            
        dates.sort()
        population = maxPopulation = maxYear = 0
        for year , change in dates:
            population +=change
            if population > maxPopulation:
                maxPopulation = population
                maxYear = year
        return maxYear
        
        
        
        
#         offset = 1950
#         bucket = list[100]
#         for i in logs:
#             [birth, death] = i
#             for i in range(birth, death):
#                 bucket[i] = bucket[i] +1
#         maxPopulation = 0
#         maxYear = 0
#         for i in range(0, len(bucket)):
#             if bucket[i] > maxPopulation:
#                 maxPopulation = bucket[i]
#                 maxYear = i
#         return maxYear + offset
    
