class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #We have to use SET for this Question
        #Siliding Window technique
        #l,r pointers l=0,r is keeping moving
        #if any dulipate in set then remove it from left and then increment left pointer by one
        #if not then add right to charset
        #res should be r+l-1
        
        
        
        
        
        
        
        
        """
        l,r=0,0
        charset=set()
        res=0
        for i in range(len(s)):
            if s[i]!=s[r]:
                r+=1
                charset.add(s[r])
            else:
                r=l
                charset.remove(s[l])
                
                
        res=max(res,r-l+1)
        return res
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        charset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res=max(res,r-l+1)
        return res
              
                    
        