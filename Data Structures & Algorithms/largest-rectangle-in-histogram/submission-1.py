class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        heights.append(0)
        ans = 0
        l = 0
        for r in range(len(heights)):
            while st and heights[st[-1]] > heights[r]:
                h = st.pop()
                l = st[-1]
                ans  = max(ans,heights[h] * (r - l - 1) )
            st.append(r)
        return ans
