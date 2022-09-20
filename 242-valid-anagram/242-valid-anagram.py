class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if len(s)!=len(t):
            return False
        for i in s:
            if i in t:
                return True
        return False
        """
        #successfilly worked

        s=sorted(s)
        t=sorted(t)
        return s==t  
    