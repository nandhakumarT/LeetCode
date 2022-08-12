class Solution:
    def maxArea(self, height: List[int]) -> int:
        #edge case
        h=height
        if len(h)==0:
            return 0
        if len(h)==1:
            return h
        
        l,r=0,len(h)-1
        maxwater=0
        
#by find the min height between the left and right pointer

#then find the distance between the left and right pointer by subtracting the left pointer vlaue and right pointer value

#then multiple both min height and maxdistance and find the max value of individual result

        while l<r:
            res=r-l#abs is to get poistive output
            minheight=min(h[l],h[r])
            maxwater=max(maxwater,minheight*res)
            if h[l]<h[r]:
                l+=1
            elif h[l]>h[r]:
                r-=1
            else:
                l+=1
                r-=1   
        return maxwater
    
        