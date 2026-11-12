class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            indegree[cur] += 1
        q = deque([c for c in range(numCourses) if indegree[c] == 0])
        ans = []
        res = 0
        while q:
            pre = q.popleft()
            ans.append(pre)
            for cur in graph[pre]:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    q.append(cur)
            res += 1
        return ans if res == numCourses else []