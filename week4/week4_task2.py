class Node(object):
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=0

class AVLTree(object):
    def __init__(self):
        self.root=None
    def find(self,key):
        if self.root is None:
            return None
        else:
            return self._find(key,self.root)
    def _find(self,key,node):
        if node is None:
            return None
        elif key<node.key:
            return self._find(key,self.left)
        elif key>node.key:
            return self._find(key,self.right)
        else:
            return node
    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)
    def _findMin(self,node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node
    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)
    def _findMax(self,node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node
    def height(self,node):
        if node is None:
            return -1
        else:
            return node.height
    def LLrotate(self,node):
        k1=node.left
        node.left=k1.right
        k1.right=node
        node.height=max(self.height(node.right),self.height(node.left))+1
        k1.height=max(self.height(k1.left),node.height)+1
        return k1
    def RRrotate(self,node):
        k1=node.right
        node.right=k1.left
        k1.left=node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1
    def RLrotate(self,node):
        node.right=self.LLrotate(node.right)
        return self.RRrotate(node)
    def LRrotate(self,node):
        node.left=self.RRrotate(node.left)
        return self.LLrotate(node)

    def put(self,key):
        if not self.root:
            self.root=Node(key)
        else:
            self.root=self._put(key,self.root)
    def _put(self,key,node):
        if node is None:
            node=Node(key)
        elif key<node.key:
            node.left=self._put(key,node.left)
            if (self.height(node.left)-self.height(node.right))==2:
                if key<node.left.key:
                    node=self.LLrotate(node)
                else:
                    node=self.LRrotate(node)
        elif key>node.key:
            node.right = self._put(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key < node.right.key:
                    node = self.RLrotate(node)
                else:
                    node = self.RRrotate(node)
        node.height=max(self.height(node.left),self.height(node.right))+1
        return node
lth = int(input())
sequence = [int(x) for x in input().split()]
myAVL = AVLTree()
for i in range(lth):
    key = sequence[i]
    myAVL.put(key)

print(myAVL.root.key)
