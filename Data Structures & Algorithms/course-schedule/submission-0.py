class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preCourse = {i:[] for i in range(numCourses)}
        visited = set()
        for crs, pre in prerequisites:
            preCourse[crs].append(pre)
        
        def dfs(crs):
            if preCourse[crs] == []:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in preCourse[crs]:
                if not dfs(pre):
                    return False
                dfs(pre)
            visited.remove(crs)
            preCourse[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
