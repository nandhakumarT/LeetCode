class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l=0
        
        for r in nums:
            if r!=nums[l]:        
                l+=1
                nums[l]=r           
        return l+1
    
    