class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        nums1[m:]=nums2
        nums1.sort()
     
        
        
        """
        if m==0 and n==0:
            return None
        elif m==1 and n==0:
            return m
        elif m==0 and n==1:
            return n
        
        res=[]
        
        for i in range(m-1):
            for j in range(n-1):
                if nums1[i]<nums2[j]:
                    res.append(nums1[i])
                elif nums1[i]==nums2[j]:
                    i+=1
                else:
                    res.append(nums2[j])
        return res
        """            