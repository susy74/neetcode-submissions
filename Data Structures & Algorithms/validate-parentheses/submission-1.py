class Solution:
    def isValid(self, s: str) -> bool:
        D = {
            '[': ']',
            '(': ')',
            '{': '}'
        }
        st = []
        for c in s:
            if c in D:
                st.append(D[c])

            elif st and st[-1] == c:
                st.pop()
            else:
                return False
        return True if not st else False
        