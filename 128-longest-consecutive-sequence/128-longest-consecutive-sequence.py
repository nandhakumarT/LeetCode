class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(nums)
        c1=1
        c=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i]+1==nums[i+1]:
                c+=1
                c1=max(c1,c)
            else:
                c=1
        return c1
        
        """
        res=[]
        i=0
        for i in range(len(nums)):
            if i<len(nums):
                if i+1 in set(nums):
                    res.append(i+1)
                else:
                    i+=1
        return len(res)
        """
                