class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        res = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                index_minh = stack.pop()
                width = i - stack[-1] - 1
                res = max(res, heights[index_minh] * width)
            stack.append(i)
        return res
