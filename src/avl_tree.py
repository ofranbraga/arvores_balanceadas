#FRANCISCO CLAUDIONOR DE BARROS BRAGA
#KAMILA SOFIA DE OLIVEIRA SARMANHO

class Node:
    def __init__(self, chave : int):
        self.no = chave
        self.altura : int = 1
        self.filho_esq : Node | None = None
        self.filho_dir : Node | None = None

class arvore_avl:
    def __init__(self):
        self.raiz : Node | None = None

    def altura_node(self, no : Node):
        "Função para retornar a altura de cada sub-árvore"

        if no is None:
            return 0
        return no.altura
    
    def fator_balanceamento(self, no : Node):
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

        return node

    def min_Node(self, node : Node):
        """Função para encontrar o menor valor de uma árvore binária.
        Será utilizada para encontrar o sucessor de um nó para realizar a remoção de um nó com dois filhos"""
        
        no_atual = node

        while not no_atual:
            no_atual = no_atual.filho_esq
        return no_atual

    def deletar(self, chave : int):
        "Função principal para deletar um nó em uma árvore binária"

        self.raiz = self.deletar_Node(self.raiz, chave)

    def deletar_Node(self, node : Node, chave : int):
        """Função auxiliar para deletar um nó, seguindo a definição. Verifica-se em qual posição o nó está.
        Caso o nó seja uma folha: verifica apenas o balanceamento da árvore;
        Caso o nó tenha apenas um filho: o filho assume o lugar do pai e verifica o balanceamento da árvore;
        Caso o nó tenha dois filhos: o sucessor, ou o nó mais a esquerda da sub-árvore à direita, assume o lugar do pai e
        verifica o balanceamento."""

        if node is None:
            return

        if chave < node.no:
            node.filho_esq = self.deletar_Node(node.filho_esq, chave)
        elif chave > node.no:
            node.filho_dir = self.deletar_Node(node.filho_dir, chave)
        
        else:
            if not node.filho_esq:
                temp = node.filho_dir
                node = None
                return temp
            elif not node.filho_dir:
                temp = node.filho_esq
                node = None
                return temp
        
            temp = self.min_Node(node.filho_dir)
            node.no = temp.no
            node.filho_dir = self.deletar_Node(node.filho_dir, temp.no)
        
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

        return node
    
    def procurar_elemento(self, chave : int):
        "Função principal para procurar um elemento em uma árvore binária"
        
        return self.procurar_elemento_Node(self.raiz, chave)

    def procurar_elemento_Node(self, node : Node, chave : int):
        """Função auxiliar recursiva de busca.
        Caso um elemento esteja na árvore, retornará True;
        Caso não, retornará False. 
        """

        if node is None:
            return False
        elif node.no == chave:
            return True
        elif chave < node.no:
            return self.procurar_elemento_Node(node.filho_esq, chave)
        else:
            return self.procurar_elemento_Node(node.filho_dir, chave)
        
    def inserir_lista(self, array : list[int]):
        """Função para inserir uma lista de n elementos.
        Apesar de aumentar a complexidade do algoritmo, serve para facilitar na demonstração do código"""
        for n in array:
            self.inserir(n)
            self.to_String()
            print('')
            
    def remover_lista(self, array : list[int]):
        """Função para remover uma lista de n elementos.
        Apesar de aumentar a complexidade do algoritmo, serve para facilitar na demonstração do código"""
        for n in array:
            self.deletar(n)
            self.to_String()
            print('')

    def to_String(self, nivel : int = 0):
        "Função principal para printar a árvore binária"

        self.to_String_Node(self.raiz, nivel)
    
    def to_String_Node(self, no_atual : Node, nivel : int):
        """Função auxiliar para printar a árvore no terminal.
        A primeira linha será a raíz. Normalmente, a primeira linha após a raíz será a sub-árvore a esquerda
        e a segunda, a sub-árvore à direita"""
        
        # if nivel == 0 and no_atual is None:
        #     no_atual = self.raiz
        
        if no_atual is None:
            return

        prefixo = " " * (nivel - 1) * 4 + "├─ " if nivel > 0 else ""
        print(f"{prefixo}{no_atual.no}")
                
        self.to_String_Node(no_atual.filho_esq, nivel + 1)
        self.to_String_Node(no_atual.filho_dir, nivel + 1)

avl = arvore_avl()

# avl.inserir(10)
# avl.inserir(20)
# avl.inserir(12)
# avl.inserir(15)
# avl.inserir(21)
# avl.inserir(23)
# print(avl.procurar_elemento(20))
# avl.to_String()

# avl.deletar(20)
# print(avl.procurar_elemento(20))
# avl.to_String()

avl.inserir_lista([1, 2, 3, 4, 5, 6])

avl.remover_lista([2, 5])