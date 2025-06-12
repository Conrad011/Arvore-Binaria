
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Inserção
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    # Remoção
    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            minLargerNode = self._getMin(node.right)
            node.key = minLargerNode.key
            node.right = self._remove(node.right, minLargerNode.key)
        return node

    def _getMin(self, node):
        while node.left:
            node = node.left
        return node

    # Percursos
    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, node):
        if node is None:
            return []
        return self._inOrder(node.left) + [node.key] + self._inOrder(node.right)

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, node):
        if node is None:
            return []
        return [node.key] + self._preOrder(node.left) + self._preOrder(node.right)

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, node):
        if node is None:
            return []
        return self._postOrder(node.left) + self._postOrder(node.right) + [node.key]

    # Verificar se é estritamente binária
    def isStrictlyBinary(self):
        return self._isStrictlyBinary(self.root)

    def _isStrictlyBinary(self, node):
        if node is None:
            return True
        if (node.left is None) != (node.right is None):
            return False
        return self._isStrictlyBinary(node.left) and self._isStrictlyBinary(node.right)

    # Verificar se é cheia
    def isFull(self):
        return self._isFull(self.root)

    def _isFull(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left and node.right:
            return self._isFull(node.left) and self._isFull(node.right)
        return False

    # Verificar se é completa
    def isComplete(self):
        if self.root is None:
            return True
        queue = [(self.root, 0)]
        i = 0
        while i < len(queue):
            node, index = queue[i]
            i += 1
            if node:
                queue.append((node.left, 2 * index + 1))
                queue.append((node.right, 2 * index + 2))
        return queue[-1][1] == len(queue) - 1

    # Altura da árvore (nível máximo)
    def getLevel(self):
        return self._getLevel(self.root)

    def _getLevel(self, node):
        if node is None:
            return 0
        return 1 + max(self._getLevel(node.left), self._getLevel(node.right))

    # Grau de um nó específico
    def getNodeDegree(self, key):
        node = self._search(self.root, key)
        if node is None:
            return -1
        degree = 0
        if node.left:
            degree += 1
        if node.right:
            degree += 1
        return degree

    # Pesquisa
    def search(self, key):
        return self._search(self.root, key) is not None

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)


tree = BinaryTree()
for key in [10, 5, 20, 3, 7, 15, 25]:
    tree.insert(key)

print("In-order:", tree.inOrder())
print("Pré-ordem:", tree.preOrder())
print("Pós-ordem:", tree.postOrder())

print("É estritamente binária?", tree.isStrictlyBinary())
print("É cheia?", tree.isFull())
print("É completa?", tree.isComplete())

print("Altura da árvore:", tree.getLevel())
print("Grau do nó 10:", tree.getNodeDegree(10))
print("Existe o elemento 15?", tree.search(15))

tree.remove(10)
print("In-order após remoção:", tree.inOrder())
