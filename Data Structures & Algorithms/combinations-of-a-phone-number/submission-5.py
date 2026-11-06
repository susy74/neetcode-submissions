class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        H = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # print(H[digits[0]])
        ans = []
        tmp = []
        def dfs(i):
            if i == len(digits):
       
                ans.append(''.join(tmp))
                return
            for c in H[digits[i]]:
                tmp.append(c)
                dfs(i + 1)
                tmp.pop()
                
        if digits:
            dfs(0)
        return ans



