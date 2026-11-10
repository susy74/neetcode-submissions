class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        T = Counter(tasks)
        H = []
        for v, f in T.items():
            heapq.heappush(H, (-f))
        
        q = deque()
        time = 0
        while H or q:
            time += 1
            if not H: 
                time = q[0][1]
            else:
                f = heapq.heappop(H)
                f += 1
                if f != 0: 
                    q.append((f, time + n))
            if q and q[0][1] == time:
                
                heapq.heappush(H, q.popleft()[0])
        return time



