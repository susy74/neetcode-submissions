class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def bk(r, c, word):
            if len(word) == 0:
                return True
            if min(m, n) < 0 or r >= m or c >= n or board[r][c] != word[0]:
                return False
            tmp = board[r][c]
            board[r][c] = "#"
            res = (bk(r + 1, c, word[1:])
            or bk(r - 1, c, word[1:])
            or bk(r, c + 1, word[1:])
            or bk(r, c - 1, word[1:]))
            board[r][c] = tmp
            return res
        
        for r in range(m):
            for c in range(n):
                if bk(r, c, word):
                    return True
        return False


