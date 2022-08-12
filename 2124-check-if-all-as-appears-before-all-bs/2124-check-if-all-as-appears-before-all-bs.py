class Solution:
    def checkString(self, s: str) -> bool:
        
        ls=list(s)
        maxidxa=-1
        if ls.count('a')==0:
            return True
        if ls.count('b')==0:
            return True
        if s.rindex("a")>s.index("b"):
            return False
        return True
    
        """  
        time=59ms
        a = [i for i, val in enumerate(s) if val == 'a']
        b = [i for i, val in enumerate(s) if val == 'b']
        if len(a) == 0 or len(b) == 0:
            return True
        else:
            return max(a) < min(b)
        """
        """
        time=48ms
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
       
        """
        time=72ms
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