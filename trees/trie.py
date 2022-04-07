class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertTrie(self, word):
        currentNode = self.root
        for i in word:
            ch = i
            node = currentNode.children.get(ch)
            if node == None:
                node = Trie()
                currentNode.children.update({ ch: node })
            currentNode = node
        currentNode.endOfString = True
        print("The node has been successfully inserted in the trie")
            

newTrie = Trie()
newTrie.insertTrie("app")