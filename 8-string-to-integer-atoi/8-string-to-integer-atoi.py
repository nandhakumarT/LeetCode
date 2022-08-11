class Solution:
    def myAtoi(self, s:str) -> int:
        
 
        # Remove any additional spaces before the given string
        s = s.lstrip()
        
        # If string is empty return 0
        if len(s) == 0:
            return 0

        # String index from where the processing should start
        start = 0
        
        # Handling numbers with +/- sign
        sign_multiplier = 1
        if s[0] == '-': # Handling for negative sign numbers
            sign_multiplier = -1
            start = 1
        elif s[0] == '+': # Handling for signed positive sign number
            start = 1

        result = 0

        index = start
        while index < len(s):
            # Handling for non numeric values
            if not('0' <= s[index] <= '9'):
                return result * sign_multiplier

            # Calculate the result for current iteration
            result = result * 10 + ord(s[index]) - ord('0')

            # Check if result exceeds MinInt32 or MaxInt32
            min_int_32 = 2 ** 31
            if result * sign_multiplier <= -min_int_32:
                return -min_int_32
            elif result * sign_multiplier >= min_int_32-1:
                return min_int_32-1
            index+=1

        return result * sign_multiplier
    
        """
        #to remove white space use strip
        s=s.strip()
        
        #edge case
        if not s:
            return 0
        
        #assgin value
        negative=False
        res=0
        
        #symbol(-,+)
        if s[0]=="-":
            negative= True
        if s[0]=="+":
            negative=False
        #checking numeric using .isnumeric
        elif not s[0].isnumeric:
            return 0
        else:
            res=ord(s[0])-ord("0")
            
        for i in range(1,len(s)):
            if s[i].isnumeric():
                res=res*10 + (ord(s[i])-ord("0"))
                #out of range
                if not negative and res>=(2**31 -1):
                    return (2**31 -1)
                if negative and res>=(-2**31):
                    return -2**31
            else:
                break
        if not negative:
            return res
        else:
            return -res
            
            
        """
        """
        max_int=(2**31)-1
        min_int=-2**31
        i=0
        res=0
        negative=1
        
        #whitespace
        while i<len(s) and s[i]==' ':
            i+=1
        
        #symbol
        if i<len(s) and s[i]=='-':
            i+=1
            negative=-1
        elif i<len(s) and s[i]=='+':
            i+=1
            
        #checking numbers
        checker = set('0123456789')
        while i < len(s) and s[i] in checker:  
            
            #edge case
            #out of range
            if res > max_int / 10 or (res == max_int / 10 and int(s[i]) > 7):
                
                return max_int if negative == 1 else min_int 
            res = res * 10  + int(s[i])
            i += 1
                
                
        return res*negative
        """
        
        
      
        
        #if s== "-":
        #    for i in range(1,len(s)):
        #        res=res*10+(ord(s)-ord(s[0]))
         #       res=res*-1
          #  return res
        #for i in range(len(s)):
         #   res=res*10+(ord(s)-ord(s[0]))
        #return res
        
        #if res>(-2**31) and res<(2**31 -1):
         #   return res
        
        
        
        
