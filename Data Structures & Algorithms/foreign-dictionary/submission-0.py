class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = collections.defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        for first, second in zip(words, words[1:]):
            for c, d in zip(first, second):
                if c != d:
                    if d not in graph[c]:
                        indegree[d] += 1
                        graph[c].add(d)
                    break
            else:               
                if len(first) > len(second):
                    return ''   
            
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for d in graph[c]:
                indegree[d] -= 1
                if indegree[d] == 0:
                    q.append(d)
        if len(res) < len(indegree):
            return ''
        return ''.join(res)