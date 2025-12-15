import sys

VERMELHO = 1
PRETO = 0

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.parent = None
        self.left = None
        self.right = None
        self.color = PRETO

class ArvoreRubroNegra:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = PRETO
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def print_helper(self, currPtr, indent, last):
        if currPtr != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "VERMELHO" if currPtr.color == VERMELHO else "PRETO"
            print(f"{currPtr.valor}({s_color})")
            self.print_helper(currPtr.left, indent, False)
            self.print_helper(currPtr.right, indent, True)
        
    def mostrar_arvore(self, titulo="Estado atual da Árvore"):
        print(f"\n--- {titulo} ---")
        if self.root == self.TNULL:
                print("Árvore vazia")
        else:
            self.print_helper(self.root, "", True)
        print("-" * 30)

    def left_rotate(self, x):
        print(f"\nRotacionando à esquerda sobre o pivô {x.valor}")
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        print(f"\nRotacionando à direita sobre o pivô {x.valor}")
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inserir(self, key):
        node = Node(key)
        node.parent = None
        node.valor = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = VERMELHO

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.valor < x.valor:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.valor < y.valor:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = PRETO
            return
            
        if node.parent.parent is None:
            return
            
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == VERMELHO:
            print(f"\nConflito: Nó {k.valor} e Pai {k.parent.valor} são VERMELHOS")

            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left #tio
                if u.color == VERMELHO:
                    print(f"   -> Caso 1: Tio {u.valor} é VERMELHO. Deve mudar a cor.")
                    u.color = PRETO
                    k.parent.color = PRETO
                    k.parent.parent.color = VERMELHO
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        print(f"   -> Caso 2: Tio PRETO e Tio PRETO e 'joelho' (triângulo). Rotação Direita no pai.")
                        k = k.parent
                        self.right_rotate(k)
                        self.mostrar_arvore("árvore após rotação direita (intermediaria)")

                    print(f"   -> Caso 3: Tio PRETO e linha reta. recolorir e rotação esquerda no avô.")
                    k.parent.color = PRETO
                    k.parent.parent.color = VERMELHO
                    self.left_rotate(k.parent.parent)
                    self.mostrar_arvore("árvore após rotação esquerda (final)")
            else:
                u = k.parent.parent.right #tio
                if u.color == VERMELHO:
                    print(f"   -> Caso 1: tio {u.valor} é VERMELHO. deve mudar a cor.")
                    u.color = PRETO
                    k.parent.color = PRETO
                    k.parent.parent.color = VERMELHO
                    k = k.parent.parent
                    self.mostrar_arvore("árvore apos mudar cor")
                else:
                    if k == k.parent.right:
                        print(f"   -> Caso 2: tio PRETO e 'joelho' (triângulo). rotação esquerda no pai.")
                        k = k.parent
                        self.left_rotate(k)
                        self.mostrar_arvore("árvore após rotação esquerda (intermediaria)")

                    print(f"   -> Caso 3: Tio PRETO e Linha Reta. Solução: Recolorir e Rotação Direita no avô.")
                    k.parent.color = PRETO
                    k.parent.parent.color = VERMELHO
                    self.right_rotate(k.parent.parent)
                    self.mostrar_arvore("árvore após rotação direita (final)")

            if k == self.root:
                break
        self.root.color = PRETO

    #remoção
    def rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
    
    def remover(self, key):
        z = self.search_helper(self.root, key)
        if z == self.TNULL:
            print(f"chave {key} não encontrada")
            return
        
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x= z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == PRETO:
            self.fix_delete(x)
        print(f"elemento {key} removido")

    def fix_delete(self, x):
        while x != self.root and x.color == PRETO:
            if x == x.parent.left:
                s = x.parent
                if s.color == VERMELHO:
                    s.color = PRETO
                    x.parent.color = VERMELHO
                    self.left_rotate(x.parent)
                    s = x.parent.right
                
                if s.left.color == PRETO and s.right.color == PRETO:
                    s.color = VERMELHO
                    x = x.parent
                else:
                    if s.right.color == PRETO:
                        s.left.color = PRETO
                        s.color = VERMELHO
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = PRETO
                    s.right.color = PRETO
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == VERMELHO:
                    s.color = PRETO
                    x.parent.color = VERMELHO
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == PRETO and s.left.color == PRETO:
                    s.color = VERMELHO
                    x = x.parent
                else:
                    if s.left.color == PRETO:
                        s.right.color = PRETO
                        s.color = VERMELHO
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = PRETO
                    s.left.color = PRETO
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = PRETO
    
    def search_helper(self, node, key):
        if node == self.TNULL or key == node.valor:
            return node
        if key < node.valor:
            return self.search_helper(node.left, key)
        return self.search_helper(node.right, key)
    
    def pesquisar(self, k):
        res = self.search_helper(self.root, k)
        return res != self.TNULL
    
    def menu():
        arvore = ArvoreRubroNegra()

        while True:
            print("\n" + "="*40)
            print("   GERENCIADOR DE ÁRVORE RUBRO-NEGRA")
            print("="*40)
            print("1. Inserir elemento (Ver rotações)")
            print("2. Remover elemento")
            print("3. Pesquisar elemento")
            print("4. Mostrar árvore completa")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                try:
                    val = int(input("Digite o número inteiro para inserir: "))
                    print(f"\n>>> Tentando inserir {val}...")
                    arvore.inserir(val)
                    arvore.mostrar_arvore("Árvore Final após Inserção")
                except ValueError:
                    print("Digite um numero valido")

            elif opcao == "2":
                try:
                    val = int(input("Digite o número inteiro para remover: "))
                    arvore.remover(val)
                    arvore.mostrar_arvore()
                except ValueError:
                    print("Numero invalido")

            elif opcao == "3":
                try:
                    val = int(input("Digite o número inteiro para pesquisar: "))
                    encontrado = arvore.pesquisar(val)
                    print(f"resultado: {'encontrado' if encontrado else 'não encontrado'}")
                except ValueError:
                    print("Numero invalido")

            elif opcao == "4":
                arvore.mostrar_arvore()

            elif opcao == "5":
                print("Saindo...")
                break
            
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    ArvoreRubroNegra.menu()