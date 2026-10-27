class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posdiag, negdiag = set(), set(), set()
        board = [['.'] * n for _ in range(n)]
        res = []
        def bk(r):
            if r == n:
                tmp = [''.join(r) for r in board]
                res.append(tmp)
                return

            for c in range(n):
                if (c in cols or (r + c) in posdiag or (r - c) in negdiag
                or board[r][c] == "Q"):
                    continue
                board[r][c] = "Q"
                cols.add(c)
                posdiag.add(r + c)
                negdiag.add(r - c)
                bk(r + 1)
                board[r][c] = "."
                cols.remove(c)
                posdiag.remove(r + c)
                negdiag.remove(r - c)
 
        bk(0)
        return res
            