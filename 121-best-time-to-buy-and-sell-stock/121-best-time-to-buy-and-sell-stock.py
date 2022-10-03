class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        res=0
        max_p=0
        
        while r<len(prices):
            res=prices[r]-prices[l]
            if prices[l]<prices[r]:
                max_p=max(res,max_p)
            else:
                l=r
            r+=1
        return max_p
    
    
    

                
        
            
            