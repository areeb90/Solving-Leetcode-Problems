class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # sett = set()
        # for i in arr:
        #     if i/2 in sett or i*2 in sett:
        #         return True
        #     sett.add(i)
        # return False
        
        l = []
        for i in arr:
            if i/2 in l or i*2 in l:
                return True
            l.append(i)
        return False