class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
    
        g=len(nums)/3
        
        if len(nums)==1 and len(nums)==2:
            return nums
                
        nums=sorted(nums)
        res=[]
        for i in set(nums):
            if nums.count(i)>g:
                res.append(i)
        return res
                
        """       
        def majorityElement(self, nums: List[int]) -> List[int]:
        greaterthan = len(nums)/3
        ans = []
        for n in set(nums):
            if nums.count(n) > greaterthan:
                ans.append(n)
        return ans
        """