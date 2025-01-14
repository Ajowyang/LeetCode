class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        #a dictionary-like object where the default value for any missing key is an empty set
        rows = defaultdict(set)
        #a dictionary-like object where the default value for any missing key is an empty set
        squares = defaultdict(set)  
        #a dictionary-like object where the default value for any missing key is an empty set

        for row_ndx in range(9):
            #for every row (9 total)
            for col_ndx in range(9):
            #for every column in that row (9 total)
                    sq = board[row_ndx][col_ndx]
                    #our current square in the board
                    if sq == '.':
                        continue
                        #if square is blank go to the next
                    if (sq in rows[row_ndx] or sq in cols[col_ndx] or sq in squares[(row_ndx // 3, col_ndx // 3)]):
                        #if this square is in the same row, same column, or same square
                        return False
                        #return False: invalid sudoku
                    
                    cols[col_ndx].add(sq)
                    #add sq to current column
                    rows[row_ndx].add(sq)
                    #add sq to current row
                    squares[(row_ndx // 3, col_ndx // 3)].add(sq)
                    #add sq to current square

        return True