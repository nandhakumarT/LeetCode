class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]==nums[j]:
                    return True
        return False
        """     
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
            
            
            
            