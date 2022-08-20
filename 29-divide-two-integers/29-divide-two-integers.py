class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
    
        sign = [-1,1][(dividend > 0) == (divisor > 0)]
        
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        
        while dividend >= divisor: #1
            doubling = 1
            cur_divisor = divisor
            while (cur_divisor<<1) <= dividend: #2
                cur_divisor <<= 1
                doubling <<= 1
            dividend -= cur_divisor #3
            res += doubling
        
        return min(max(-2147483648, res*sign), 2147483647) 
    
    
    # idea: counting how many doubling divisor we can substract from dividend.
    
    #1: conduct unless shrinking dividend wouldn't be lower than divisor
    
    #2: double probable divisor unless it wouldn't be higher than dividend
    
    #3: decrease dividend, and count how many doubling we had done during this step
    
    # repeat from 1