class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
       
        if needle in haystack:
            haystack=haystack.replace(needle,'*')
            return haystack.index('*')
        
#       if needle is an emply string:
        elif needle.isalpha()==False:
            return 0
        
        else:
            return -1
        