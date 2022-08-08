class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        r=len(grid)
        l=len(grid[0])
        
        for i in range(r):
            for j in range(l):
                if (i==j or i==l-j-1):
                    if grid[i][j]==0:
                        return False
                else:
                    if grid[i][j]!=0:
                        return False
        return True
        