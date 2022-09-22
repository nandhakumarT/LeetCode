class Solution:
    def isHappy(self, n: int) -> bool:
        
        while len(str(n))>1:
            n=sum(int(i)*int(i) for i in str(n))
        return n==1 or n==7
 
                