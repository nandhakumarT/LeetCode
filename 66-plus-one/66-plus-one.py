class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        if len(digits) is None:
            return
            
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9: 
                digits[i]=0
                
            else:
                digits[i]=digits[i]+1
                break
        else:
            return [1]+digits
        return digits
                