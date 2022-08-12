class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==0 or strs is None:
            return ""
        
        res=""
        #finding the minimum length of the string in the list of strings
        minlen=len(strs[0])
        for i in range(1,len(strs)):
            minlen=min(minlen,len(strs[i]))
        
        #finding the current string and store for comparing
        for i in range(0,minlen):
            current=strs[0][i]
        #comparing the first string with other string    
            for j in range(0,len(strs)):
                if strs[j][i]!=current:
                    return res
            res+=current
        return res
        
        
    