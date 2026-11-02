# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        H = []
        for idx, l in enumerate(lists):
            
            if l:
                heapq.heappush(H, (l.val, idx, l))
 
        dummy = ListNode(-1)
        cur = dummy
        while H:
            val, idx, l = heapq.heappop(H)
            cur.next = ListNode(val)
            cur = cur.next
            if l.next:
                heapq.heappush(H, (l.next.val, idx, l.next))
        return dummy.next

