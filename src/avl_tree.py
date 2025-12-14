class Node:
    def __init__(self, chave : int):
        self.no = chave
        self.altura : int = 1
        self.filho_esq : Node | None = None
        self.filho_dir : Node | None = None

class arvore_avl:
    def __init__(self):
        self.raiz : Node | None = None

    def altura_node(self, no):
        "Função para retornar a altura de cada sub-árvore"

        if no is None:
            return 0
        return no.altura
    
    def fator_balanceamento(self, no):
        """Função para verificar o balanceamento da árvore
        Caso o FB (Fator de Balanceamento) seja maior que 1 ou menor que -1, uma rotação deverá ser aplicada"""

        if no is None:
            return 0
        return self.altura_node(no.filho_esq) - self.altura_node(no.filho_dir)

    def rotacao_esq(self, a : Node):
        "Rotação à esquerda quando o FB tende à direita"
        #        a                         b   
        #          \                     /   \
        #           b     ----->        a     c
        #          /  \                  \
        #        temp  c                 temp
        b : Node = a.filho_dir
        temp : Node = b.filho_esq

        b.filho_esq = a
        a.filho_dir = temp

        a.altura = 1 + max(self.altura_node(a.filho_esq), self.altura_node(a.filho_dir))
        b.altura = 1 + max(self.altura_node(b.filho_esq), self.altura_node(b.filho_dir))

        return b

    def rotacao_dir(self, a : Node):
        "Rotação à direita quando o FB tende à esquerda"
        #           a                        b
        #         /                        /  \
        #        b                        c    a
        #       / \                           /
        #      c  temp                       temp
        b : Node = a.filho_esq
        temp : Node = b.filho_dir

        b.filho_dir = a
        a.filho_esq = temp

        a.altura = 1 + max(self.altura_node(a.filho_esq), self.altura_node(a.filho_dir))
        b.altura = 1 + max(self.altura_node(b.filho_esq), self.altura_node(b.filho_dir))

        return b

    def inserir(self, chave : int):
        "Função principal para inserir um nó em uma árvore binária."

        self.raiz = self.inserir_Node(self.raiz, chave)

    def inserir_Node(self, node : Node, chave : int):
        """ Função auxiliar para inserir nós em uma árvore binária AVL, seguindo a definição.
        A cada inserção, verifica-se o fator de balanceamento e se é necessário aplicar uma rotação.
        Rotação à direita: Quando o FB é 2 e o FB de sua sub-árvore à esquerda é 1;
        Rotação duplamente à direita: Quando o FB é 2 e o FB de sua sub-árvore à esquerda é -1
        Rotação à esquerda: Quando o FB é -2 e o FB de sua sub-árvore à direita é -1; 
        Rotação duplamente à esquerda: Quando o FB é -2 e o FB de sua sub-árvore à direita é 1"""

        if node is None:
            return Node(chave)

        if chave < node.no:
            node.filho_esq = self.inserir_Node(node.filho_esq, chave)

        elif chave > node.no:
            node.filho_dir = self.inserir_Node(node.filho_dir, chave)

        node.altura = 1 + max(self.altura_node(node.filho_esq), self.altura_node(node.filho_dir))
        balanceamento = self.fator_balanceamento(node)

        # Rotação à direita
        if balanceamento > 1 and self.fator_balanceamento(node.filho_esq) >= 0:
            return self.rotacao_dir(node)
        
        # Rotação duplamente à direita
        if balanceamento > 1 and self.fator_balanceamento(node.filho_esq) < 0:
            node.filho_esq = self.rotacao_esq(node.filho_esq)
            return self.rotacao_dir(node)

        # Rotação à esquerda
        if balanceamento < -1 and self.fator_balanceamento(node.filho_dir) < 0:
            return self.rotacao_esq(node)
        
        # Rotação duplamente à direita
        if balanceamento < -1 and self.fator_balanceamento(node.filho_dir) >= 0:
            node.filho_dir = self.rotacao_dir(node.filho_dir)
            return self.rotacao_esq(node)

        print(node.no, node.filho_dir, node.filho_esq)
        return node

    def toString(self, no_atual = None, nivel = 0):
        "Função para printar a árvore no terminal."
        if nivel == 0 and no_atual is None:
            no_atual = self.raiz
        
        if no_atual is None:
            return

        prefixo = " " * (nivel - 1) * 4 + "├─ " if nivel > 0 else ""
        print(f"{prefixo}{no_atual.no}")
                
        self.toString(no_atual.filho_esq, nivel + 1)
        self.toString(no_atual.filho_dir, nivel + 1)

avl = arvore_avl()

avl.inserir(10)
avl.inserir(20)
avl.inserir(12)

avl.toString()