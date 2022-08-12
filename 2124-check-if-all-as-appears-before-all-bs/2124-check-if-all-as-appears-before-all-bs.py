class Solution:
    def checkString(self, s: str) -> bool:
        
        i=0
        while s[i]=='a':
            i+=1
            if i==len(s):
                break
        while i<len(s):
            if s[i]=='a':
                return False
            i+=1
        return True
       
        """
        l,r=0,len(s)-1
        if s==" ":
            return False
        for i in range(len(s)-1):
            while l<r:
                if s[l]=='a' and s[r]=='b':
                    l+=1
                    r-=1
                elif s[l]!='a' and s[r]=='b':
                    r-=1
                elif s[l]=='a' and s[r]!='b':
                    l+=1
                else:
                    return False
         return True
         """