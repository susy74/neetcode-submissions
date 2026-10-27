class TreeNode:
    def __init__(self):
        self.child = collections.defaultdict(TreeNode)
        self.isword = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.child[letter]
        
        node.isword = True


    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            node = node.child[letter]
            if not node:
                return False
        return node.isword

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.child:
                return False
            node = node.child[letter]
        return True
        
        