class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False
class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
        node.isWord = True


    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in  node.children: return False
            node = node.children[w]
            
            # if node.isWord == False: return False
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.children: return False
            node = node.children[w]
            
            # if node.isWord == False: return False
        return True

        
        