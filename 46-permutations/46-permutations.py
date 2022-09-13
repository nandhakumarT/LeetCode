class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result=[]
        if(len(nums)==1):
            return[nums[:]]
        
        for i in range(len(nums)):
            n=nums.pop(0)#removing the first element in the list
            perms=self.permute(nums)#then re-calling the function by using self and assign to the operater perms
            
            for perm in perms:#checking whether the perm in the perms
                perm.append(n)#then adding the to perm ,the pop value will be added
            result.extend(perms)#other then pop value is added to result
            nums.append(n)#add the pop value to the nums
            
        return result
            
            