class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        res=0
        res1=4      
        if len(nums)==0:
            return [-1,-1]
        
        for i in range(len(nums)):
            if nums[i]!=target:
                res+=1
            else:
                return [res,res1]
        return[-1,-1]
        """
        
        
        
        
        l,r=0,len(nums)-1
        for i in range(len(nums)):
            if nums[l]!=target and nums[r]!=target:
                l+=1
                r-=1
            elif nums[l]==target and nums[r]!=target:
                r-=1
            elif nums[l]!=target and nums[r]==target:
                l+=1
            else:
                return[l,r]
        return [-1,-1]
                