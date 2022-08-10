class Solution:
    def reverse(self, x: int) -> int:
       # new_lst = x[::-1]
        #return new_lst
        
        
        
        #if x>(2**31): 
         #   return 0
        #if x<(2**31-1):
          #  return 0
        #res=0
        #if x<0:
         #   x=x*-1
          #  while x>0:
           #     remainder=int(math.fmod(x,10))#
            #    x=int(x/10)
             #   res=(res*10)+remainder
        #return -res
        
        #while x>0:
         #   remainder=int(math.fmod(x,10))#
         #  x=int(x/10)
           # res=(res*10)+remainder
        #return res
                    
      
        if x<(-2**31) or x>(2**31 -1):
            return 0
        if x>=0:
            if int(str(x)[::-1]) <= (2**31 -1):
                return int(str(x)[::-1])
            return 0
        if x<0:
            if -int(str(x)[-1:0:-1]) >= (-2**31):
                return -int(str(x)[-1:0:-1])
            return 0
    

        