class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        D = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i + 1 :]
                D[pattern].append(w)

        visited = set()
        q = deque()
        q.append(beginWord)
        ans = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return ans
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1 :]
                    for neigh in D[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
            ans += 1
        return 0


        
