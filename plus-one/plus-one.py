class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        toString = ''
        for i in range(len(digits)):
            toString += str(digits[i])
        t = str(int(toString)+1)
        return[i for i in t]
            