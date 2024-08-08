class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        h=collections.defaultdict(set)
        v=collections.defaultdict(set)
        square=collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):


                if board[i][j]=='.':
                    continue 
                
                if board[i][j] in h[i] or board[i][j] in v[j] or board[i][j] in square[(i//3,j//3)]: 
                    return False
                
                v[j].add(board[i][j])
                h[i].add(board[i][j])
                square[(i//3,j//3)].add(board[i][j])

        return True