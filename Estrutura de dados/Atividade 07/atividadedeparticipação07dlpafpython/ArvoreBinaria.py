from Node import Node


class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def inserir(self, Chave, valor=None):
        def inserir(node, Chave, valor):
            if node is None:
                return Node(Chave, valor)
            if Chave < node.Chave:
                node.esquerda = inserir(node.esquerda, Chave, valor)
            elif Chave > node.Chave:
                node.direita = inserir(node.direita, Chave, valor)
            else:
                node.valor = valor
            return node

        self.root = inserir(self.root, Chave, valor)

    def tam(self):
        def tam(node):
            if node is None:
                return 0
            return 1 + tam(node.esquerda) + tam(node.direita)

        return tam(self.root)

    def altura(self):
        def altura(node):
            if node is None:
                return 0
            return 1 + max(altura(node.esquerda), altura(node.direita))

        return altura(self.root)

    def min(self):
        def _min(node):
            if node.esquerda is None:
                return node
            return _min(node.esquerda)

        if self.root is None:
            return None
        return _min(self.root).Chave

    def max(self):
        def _max(node):
            if node.direita is None:
                return node
            return _max(node.direita)

        if self.root is None:
            return None
        return _max(self.root).Chave

    def internal_path_length(self):
        def _internal_path_length(node, depth=0):
            if node is None:
                return 0
            return depth + _internal_path_length(node.esquerda, depth + 1) + _internal_path_length(node.direita, depth + 1)

        return _internal_path_length(self.root)

    def emordem(self):
        def emordem(node):
            if node is None:
                return []
            return emordem(node.esquerda) + [node.Chave] + emordem(node.direita)

        return emordem(self.root)

    def posordem(self):
        def posordem(node):
            if node is None:
                return []
            return posordem(node.esquerda) + posordem(node.direita) + [node.Chave]

        return posordem(self.root)

    def preordem(self):
        def preordem(node):
            if node is None:
                return []
            return [node.Chave] + preordem(node.esquerda) + preordem(node.direita)

        return preordem(self.root)

    def largura(self):
        if self.root is None:
            return []

        queue = [self.root]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node.Chave)
            if node.esquerda:
                queue.append(node.esquerda)
            if node.direita:
                queue.append(node.direita)

        return result