class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack=[]
        closetoopen={ "}":"{" , "]":"[", ")":"("}

        for i in s:
            if i in closetoopen:
                if stack and stack[-1] == closetoopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        
        """
        #edge case
        if len(s)%2!=0:
            return False
        
        hash={ "(": ")","[": "]","{": "}"}
        res=[]
        #if add s values in hash
        for i in range(len(s)):
            if s[i] in hash:
                res.append(s[i])
            
        #if (,{,[ if this value are not present in the start of the sting
        #then pop the value and add to last_item
            else:
                if len(res)>0:
                    last_item=res.pop()
        #if hash of last_item has not present in s then return false            
                    if s[i] != hash[last_item]:
                        return False
                    
                else:
                    return False
           
        return len(res)==0
        """
            
       