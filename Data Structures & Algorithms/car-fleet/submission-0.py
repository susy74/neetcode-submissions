class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        st = []
        for p, s in sorted(zip(position, speed)):
            h = (target - p) / s
            
            while st and st[-1] <= h:
                st.pop()
            st.append(h)
    
        return len(st)