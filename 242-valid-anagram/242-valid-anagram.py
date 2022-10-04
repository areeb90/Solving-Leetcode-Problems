class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = Counter(s)
        w2 = Counter(t)
        if (len(s)== len(t)) and (w1== w2):
            return True
        else:
            return False