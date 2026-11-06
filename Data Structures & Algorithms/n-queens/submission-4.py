class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)] 
        pos, neg, col, row = set(), set(), set(), set()
        ans = []
        def dfs(r):
            if r == n:
                tmp = [''.join(r) for r in board]
                ans.append(tmp.copy())
            for c in range(n):
                if c in col or r + c in pos or r - c in neg or board[r][c] == 'Q':
                    continue
                board[r][c] = 'Q'
                pos.add((r + c))
                neg.add((r - c))
                col.add(c)
                dfs(r + 1)
                pos.remove((r + c))
                neg.remove((r - c))
                col.remove(c)
                board[r][c] = '.'
        dfs(0)
        return ans

