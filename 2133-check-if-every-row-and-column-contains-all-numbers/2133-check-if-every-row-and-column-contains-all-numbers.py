class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n=len(matrix)
        store=set([i for i in range(1,n+1)])
        
        for row in matrix:
            if set(row) != store:
                return False
            
        for col in zip(*matrix):
            if set(col)!=store:
                return False
        
        return True
            
        
        
        
        
        
"""
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        # define N
        n = len(matrix)
        # generate set of [1,N]
        store = set([i for i in range(1,n+1)])
        
        # check in row
        for row in matrix:
            if set(row) != store:
                return False
        
        # check in column
        for col in zip(*matrix):
            if set(col) != store:
                return False
            
        # all good
        return True
"""