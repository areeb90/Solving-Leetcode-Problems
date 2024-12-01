class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visit = set()
        for num in arr:
            if num*2 in visit or num/2 in visit:
                return True
            visit.add(num)
        return False

            
        return False