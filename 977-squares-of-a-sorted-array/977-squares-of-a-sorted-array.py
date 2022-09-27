class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        for i in nums:
            nums[i]=nums[i*2]
        
        return sorted(nums)
        """
        return sorted([i**2 for i in nums])
