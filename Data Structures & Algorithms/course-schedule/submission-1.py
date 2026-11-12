class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph =collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            indegree[cur] += 1
        # q = deque()
        q = deque([c for c in range(numCourses) if indegree[c] == 0])
        ans = 0
        while q:
            cur = q.popleft()
            for child in graph[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
            ans += 1
        return ans == numCourses 
                

