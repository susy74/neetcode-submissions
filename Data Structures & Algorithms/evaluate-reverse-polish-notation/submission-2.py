class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c == '+':
                st[-1] = st.pop() + st[-1]
            elif c == '*':
                num = st.pop()
                st[-1] = num * st[-1]
                

            elif c == '-':
                num = st.pop()
                st[-1] = st[-1] - num
            elif c == '/':
                num = st.pop()
                print(num)
                print(st[-1])
                st[-1] = int(st[-1] / num)
                print(st[-1])
                
            else: 
                st.append(int(c))

        return st[-1]

