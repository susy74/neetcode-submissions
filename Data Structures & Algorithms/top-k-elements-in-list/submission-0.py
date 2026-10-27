class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = collections.defaultdict(int)
        for num in nums:
            cnts[num] += 1
        H = []
        for val, freq in cnts.items():
            heapq.heappush(H,(-freq, val))
        ans = []
        while k > 0:
            _, val = heapq.heappop(H)
            ans.append(val)
            k -= 1
        return ans
            


            
    
