class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #product of individual value in the array
        """
        product=1
        res=[]
        for i in range(0,len(nums)):
            if nums[i]<0:
                nums[i]=nums[i]*-1
            product=product*nums[i]
        for j in range(0,len(nums)):
            if nums[j]<0:
                nums[j]=nums[j]*-1
            if nums[j]==0:
                j+=1
            res.append(product//nums[j])
        return res
        """
        res=[1]*len(nums)

        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res