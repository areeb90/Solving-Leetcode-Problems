class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(m, len(nums1)+1):
        #     nums1.pop(nums1[i])
        # for j in nums2[:n]:
        #     nums1.append(j)
        
        i = 0
        while i<n:
            nums1[:]=nums1[:m] + nums2
            
            i+=1
        nums1.sort()
            