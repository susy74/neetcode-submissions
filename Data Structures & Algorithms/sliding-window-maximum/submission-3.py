class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
     
        ans = []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            l = r - k + 1
            if l < 0: continue
            if q[0] < l:
                q.popleft()
            if r - l + 1 == k:
                ans.append(nums[q[0]])
        return ans
