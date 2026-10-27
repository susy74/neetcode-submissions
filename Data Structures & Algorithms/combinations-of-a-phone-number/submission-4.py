class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res =[]
        dict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def bk(i, tmp):
            if i == len(digits):
                res.append(tmp)
                return
            
            for c in dict[digits[i]]:
                bk(i + 1, tmp + c)
 
        if digits:
            bk(0, '')
        return res
                



