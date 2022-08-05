class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #TOP DOWN MEMOIZATON
        
        #Two pointer i,j at s,p
        #if start of s[i] and p[j] are equal
        #store and increment i+1
        #else j+2
        #if [i>=len(s) and j>=len(p)] , [i>=len(s) and j>=len(p)] -> TRUE
        
        cache={}
        
        def dfs(i,j):
            
            if(i,j) in cache:
                return cache[(i,j)]
            
            if i>=len(s) and j>=len(p):
                return True
            
            if j>=len(p):
                return False
            
            match=i<len(s) and (s[i]==p[j] or p[j]==".")
            
            if (j+1)<len(p) and p[j+1] =="*":
                cache[(i,j)] = (dfs(i,j+2) or 
                                (match and dfs(i+1,j)))
                return cache[(i,j)]
            
            if match:
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return False
        return dfs(0,0)
            
       # i,j=0,0
       # res=""
       # for i in range(len(s)):
       #     for j in range(len(p)):
       #         if s[i]==p[j]:
       #             res=res+(s[i])
       #           i=i+1
        #        else:
         #           j=j+2
      
