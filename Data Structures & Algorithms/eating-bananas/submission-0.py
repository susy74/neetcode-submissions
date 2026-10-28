class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = 0
        while left <= right:
            mid = (right + left) // 2
            time = 0
            for p in piles:
                time +=  math.ceil(p/mid)
            if time <= h:
                ans = right
                right= mid - 1
            else:
                
                left = mid + 1
                # ans = left
        return left
            