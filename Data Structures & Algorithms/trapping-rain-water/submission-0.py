class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        ans = 0
        for i in range(len(height)):
            while st and height[st[-1]] < height[i]:
                mid = st.pop()
                if st:
                    l = st[-1]
                    ans += (min(height[l], height[i]) - height[mid]) * (i - l - 1)

            st.append(i)
            
        return ans