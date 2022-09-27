class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        li=list(s.strip())
        li=list("".join(s.split()))
        li=list(s.replace(" ",""))
        li=list(s.replace(',',""))
        li=list(s.replace(':',""))
    
        
        m=int(len(s)/2)
        
        for l in range(len(li)-1):
            for r in range(len(li)-1):
                if l>=0 and r<len(li):
                    l=m-1
                    r=m+1
                    if li[l]!=li[r]:
                        return False
                    else:
                        continue
                        l-=1
                        r+=1
        return True
        """
        if s==" ":return True
        
        s=s.lower()
        new_s=""
        
        for i in s:
            #97 to 123 a-z, 48 to 58 0-9
            if(ord(i) in range(97,123)) or (ord(i) in range(48,58)):
                new_s+=i
            
        return new_s==new_s[::-1]
    
       