class TreeNode:
    def __init__(self):
        self.child = collections.defaultdict(TreeNode)
        self.isword = False
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.child[letter]
        node.isword = True


        
    def search(self, word: str) -> bool:
        def dfs(start, root):
            node = root
            for i in range(start, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.child.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in node.child:
                        return False
                    node = node.child[c]
            return node.isword
        return dfs(0, self.root)
        
                        

                
                

        
