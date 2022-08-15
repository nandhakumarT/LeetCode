class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hash={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}
        
        res=[]
        
        def backtrack(i,curr):
            if len(curr) == len(digits):
                res.append(curr)
                return 
            for c in hash[digits[i]]:
                backtrack(i+1,curr+c)
        
        if digits:
            backtrack(0,"")
        return res
                
        
        
        
"""        
Step 1: Created a dictionary with required mappings, and empty list to store the required mapping of the input "digits"
Step 2: check if the digits length is 0 as we need to return an empty list in that case.
Step 3: otherwise loop through the letters in the input and get the correspond value of it from the mappings dictionary.
Step 4: Then we append that value(convert it into a list) to a list.
Step 5: Finally we use the itertools product to apply product on the elements present in our combinations list.
"""                
