class Node:
    def __init__(self, chave : int):
        self.no = chave
        self.altura : int = 0
        self.filho_esq : Node | None = None
        self.filho_dir : Node | None = None

class arvore_avl:
    def __init__(self):
        self.raiz : Node | None = None

    def inserir(self, chave : int):
        """
        Função principal para inserir um nó em uma árvore binária.
        """
        if self.raiz is None:
            self.raiz = Node(chave)
        else:
            self.inserir_Node(self.raiz, chave)

    def inserir_Node(self, node : Node, chave : int):
        """ Função auxiliar para inserir nós em uma árvore binária de busca, seguindo a definição.
        Caso a nova chave inserida seja menor que o nó estamos comparado, ela irá para o lado esquerdo  
        árvore até encontrar uma folha. 
        """
        if chave < node.no:
            if node.filho_esq == None:
                node.filho_esq = Node(chave)
            else:
                self.inserir_Node(node.filho_esq, chave)
        elif node.filho_dir == None:
            node.filho_dir = Node(chave)
        else:
            self.inserir_Node(node.filho_dir, chave)

    def toString(self, no_atual = None, nivel = 0):
        if nivel == 0 and no_atual is None:
            no_atual = self.raiz
        
        if no_atual is None:
            return

        prefixo = " " * (nivel * 4) + "├─ " if nivel > 0 else ""
        print(f"{prefixo}{no_atual.no}")
                
        self.toString(no_atual.filho_esq, nivel + 1)
        self.toString(no_atual.filho_dir, nivel + 1)
            

    # def altura_Node(self):
    #     if no == None:
    #         return -1
    #     return 
    
    # def balanceamento():
    #     return altura_Node(self.no.filho_esq) - altura_Node(self.no.filho_dir)

avl = arvore_avl()

avl.inserir(4)
avl.inserir(3)
avl.inserir(2)
avl.inserir(1)
avl.inserir(7)
avl.inserir(6)
avl.inserir(5)

avl.toString()