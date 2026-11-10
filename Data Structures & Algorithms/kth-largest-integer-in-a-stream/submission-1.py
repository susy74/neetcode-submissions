class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.H = []
        for num in nums:
            heapq.heappush(self.H, num)
        print(len(self.H))
        while len(self.H) > k:
            heapq.heappop(self.H)
        self.k = k


        

    def add(self, val: int) -> int:
        heapq.heappush(self.H, val)
        if len(self.H) > self.k:
            heapq.heappop(self.H)
        return self.H[0]
        
