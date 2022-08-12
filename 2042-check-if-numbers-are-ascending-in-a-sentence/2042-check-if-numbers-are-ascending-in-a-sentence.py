class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        res=0
        w=s.split()
        
        for i in w:
            if i.isnumeric():
                if res>=int(i):
                    return False
                else:
                    res=int(i)
        return True
       
            
        

        
            
        