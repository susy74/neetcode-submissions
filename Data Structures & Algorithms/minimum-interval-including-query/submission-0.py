class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)
        minH = []
        res = {}
        i = 0
        for num in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= num:
                start, end = intervals[i]
                heapq.heappush(minH, (end - start + 1, end))
                i += 1
            while minH and minH[0][1] < num:
                heapq.heappop(minH)
            res[num] = minH[0][0] if minH else -1
        return [res[num] for num in queries]
            