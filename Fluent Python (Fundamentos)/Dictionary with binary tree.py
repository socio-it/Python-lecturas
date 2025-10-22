# Dictionary with binary tree
class Node:
    def __init__(self):
        self.value = None
        self.rigth = None
        self.left = None
        self.parent = None

class BinaryDict:
    def __init__(self):
        self.root = None
    
    def search(self, prefix):
        return self.search_recursion(prefix,self.dict)
    
    def search_recursion(self, prefix,dict):
        pass
    
    def append_word(self,word):
        if word:
            
            self.append_word(word[1:-1])

    def add(self, letter):
        if not self.root:
            node = Node()
            node.value = letter
            return node
        return self.add_recursion(self.root, letter)
    
    def add_recursion(self, node, letter):
        if not node:
            node = Node()
            node.value = letter
            return node
            
        if letter > node.value:
            self.add_recursion(node.rigth.value)
        else:
            self.add_recursion(node.left.value)
        

