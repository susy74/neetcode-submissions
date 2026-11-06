class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(open, close, tmp):
            if open == close == n:
                ans.append(tmp)
                return
            if open < n:
                dfs(open + 1, close, tmp + '(')
            if open > close:
                dfs(open, close + 1, tmp + ')')
        dfs(0, 0, '')
        return ans
            
            