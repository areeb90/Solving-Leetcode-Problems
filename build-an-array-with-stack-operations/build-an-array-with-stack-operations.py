class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        s = set(target)
        for i in range(1, target[-1] +1):
            res.append("Push")
            if i not in target:
                res.append("Pop")
        return res
        
        
#         res = []
#         for i in range(1,n+1):
#             if i in target:
#                 res.append("Push")
#             else:
#                 res.append("Push")
#                 res.append("Pop")
#             if i == target[-1]:
#                 break
            
#         return res 