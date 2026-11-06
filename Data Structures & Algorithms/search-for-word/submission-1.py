class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, w):
            if len(w) == 0: return True
            if min(r, c) < 0 or r >= m or c >= n or board[r][c] != w[0]:
                return False
            tmp = board[r][c]
            board[r][c] = '#'
            res = (dfs(r + 1, c, w[1:]) + 
            dfs(r - 1, c, w[1:]) + 
            dfs(r, c + 1, w[1:]) + 
            dfs(r, c - 1, w[1:]) )
            board[r][c] = tmp
            return res
        
        for r in range(m):
            for c in range(n):
                if dfs(r, c, word):
                    return True
        return False

            




        