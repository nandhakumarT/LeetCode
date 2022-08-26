class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        square=collections.defaultdict(set)#key-r//3,c//3
        
        for r in range(9):
            for c in range(9):
                
                if board[r][c] == ".":
                    continue
                
                if  (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in square[(r//3,c//3)]):
                        return False
                    
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        
        return True
        
        
        """"
        n=len(board)
        store=set([i for i in range(1,n+1)])
        
        for row in board:
            if set(row)==board:
                return False
            
        for col in zip(*board):
            if set(col)==board:
                return False
            
        return True
        """