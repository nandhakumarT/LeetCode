class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2!=0:
            return False
        
        hash={ "(": ")","[": "]","{": "}"}
        res=[]
        for i in range(len(s)):
            if s[i] in hash:
                res.append(s[i])
            
        
            else:
                if len(res)>0:
                    last_item=res.pop()
                    
                    if s[i] != hash[last_item]:
                        return False
                    
                else:
                    return False
           
        return len(res)==0
            
       