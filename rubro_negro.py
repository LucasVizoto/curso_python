class Node:
    def __init__(self, data):
        self.data = data  # Valor armazenado no nó
        self.color = 'R'  # Novo nó é sempre vermelho
        self.left = None  # Filho esquerdo do nó
        self.right = None  # Filho direito do nó
        self.parent = None  # Pai do nó

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)  # Nó nulo (NIL), usado para folhas
        self.TNULL.color = 'B'  # Nós nulos são pretos
        self.root = self.TNULL  # Inicialmente, a árvore está vazia
        
##------------------------------------------------------------------------------


    def insert(self, key):
        node = Node(key)  # Cria um novo nó
        node.left = self.TNULL  # O filho esquerdo inicial é o nó nulo
        node.right = self.TNULL  # O filho direito inicial é o nó nulo
        node.parent = None  # O pai inicial é None

        y = None  # 'y' será o pai do novo nó
        x = self.root  # Começa pela raiz

        while x != self.TNULL:  # Enquanto não encontrar um nó folha
            y = x  # Atualiza o pai do novo nó
            if node.data < x.data:
                x = x.left  # Desce para a esquerda
            else:
                x = x.right  # Desce para a direita

        node.parent = y  # Define o pai do novo nó
        if y is None:
            self.root = node  # Se a árvore estava vazia, o novo nó é a raiz
        elif node.data < y.data:
            y.left = node  # Coloca o novo nó à esquerda do pai
        else:
            y.right = node  # Coloca o novo nó à direita do pai

        if node.parent is None:
            node.color = 'B'  # A raiz deve ser preta
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)  # Ajusta a árvore para manter as propriedades rubro-negras

    def fix_insert(self, k):
        while k.parent.color == 'R':  # Enquanto o pai do nó é vermelho
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # O tio do nó
                if u.color == 'R':  # Caso 1: O tio é vermelho
                    u.color = 'B'  # Tio vira preto
                    k.parent.color = 'B'  # Pai vira preto
                    k.parent.parent.color = 'R'  # Avô vira vermelho
                    k = k.parent.parent  # Move o ponto de interesse para o avô
                else:
                    if k == k.parent.left:  # Caso 2: O nó é um filho à esquerda
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'B'  # Caso 3: O pai vira preto
                    k.parent.parent.color = 'R'  # O avô vira vermelho
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # O tio do nó
                if u.color == 'R':  # Caso 1: O tio é vermelho
                    u.color = 'B'  # Tio vira preto
                    k.parent.color = 'B'  # Pai vira preto
                    k.parent.parent.color = 'R'  # Avô vira vermelho
                    k = k.parent.parent  # Move o ponto de interesse para o avô
                else:
                    if k == k.parent.right:  # Caso 2: O nó é um filho à direita
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'B'  # Caso 3: O pai vira preto
                    k.parent.parent.color = 'R'  # O avô vira vermelho
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'B'  # A raiz deve ser preta

##------------------------------------------------------------------------------

    def left_rotate(self, x):
        y = x.right  # Define y
        x.right = y.left  # Transfere a subárvore à esquerda de y para a direita de x
        if y.left != self.TNULL:
            y.left.parent = x  # Atualiza o pai da subárvore transferida
        y.parent = x.parent  # Liga o pai de x a y
        if x.parent is None:
            self.root = y  # Se x era a raiz, agora y é a raiz
        elif x == x.parent.left:
            x.parent.left = y  # Se x era um filho à esquerda, y é agora o filho à esquerda
        else:
            x.parent.right = y  # Se x era um filho à direita, y é agora o filho à direita
        y.left = x  # Coloca x à esquerda de y
        x.parent = y  # Atualiza o pai de x

    def right_rotate(self, x):
        y = x.left  # Define y
        x.left = y.right  # Transfere a subárvore à direita de y para a esquerda de x
        if y.right != self.TNULL:
            y.right.parent = x  # Atualiza o pai da subárvore transferida
        y.parent = x.parent  # Liga o pai de x a y
        if x.parent is None:
            self.root = y  # Se x era a raiz, agora y é a raiz
        elif x == x.parent.right:
            x.parent.right = y  # Se x era um filho à direita, y é agora o filho à direita
        else:
            x.parent.left = y  # Se x era um filho à esquerda, y é agora o filho à esquerda
        y.right = x  # Coloca x à direita de y
        x.parent = y  # Atualiza o pai de x

##------------------------------------------------------------------------------

    def delete_node(self, data):
        self.delete_node_helper(self.root, data)  # Inicia a exclusão do nó

    def delete_node_helper(self, node, key):
        z = self.TNULL  # Nó z será o nó a ser removido
        while node != self.TNULL:  # Encontra o nó contendo o dado
            if node.data == key:
                z = node  # Encontra o nó com o valor desejado
            if node.data <= key:
                node = node.right  # Desce para a direita
            else:
                node = node.left  # Desce para a esquerda

        if z == self.TNULL:
            print("Cannot find key in the tree")  # Se não encontrar o nó, imprime uma mensagem
            return

        y = z  # y será usado para manter a cor original de z
        y_original_color = y.color  # Salva a cor original de y
        if z.left == self.TNULL:  # Se z não tem filho à esquerda
            x = z.right  # Define x como o filho direito de z
            self.rb_transplant(z, z.right)  # Substitui z pelo seu filho direito
        elif z.right == self.TNULL:  # Se z não tem filho à direita
            x = z.left  # Define x como o filho esquerdo de z
            self.rb_transplant(z, z.left)  # Substitui z pelo seu filho esquerdo
        else:
            y = self.minimum(z.right)  # Encontra o sucessor de z
            y_original_color = y.color  # Salva a cor original de y
            x = y.right  # Define x como o filho direito de y
            if y.parent == z:
                x.parent = y  # Atualiza o pai de x
            else:
                self.rb_transplant(y, y.right)  # Substitui y pelo seu filho direito
                y.right = z.right  # Move a subárvore direita de z para y
                y.right.parent = y  # Atualiza o pai da subárvore direita

            self.rb_transplant(z, y)  # Substitui z por y
            y.left = z.left  # Move a subárvore esquerda de z para y
            y.left.parent = y  # Atualiza o pai da subárvore esquerda
            y.color = z.color  # Copia a cor de z para y

        if y_original_color == 'B':
            self.fix_delete(x)  # Ajusta a árvore se necessário

    def fix_delete(self, x):
        while x != self.root and x.color == 'B':  # Enquanto x não for a raiz e for preto
            if x == x.parent.left:  # Se x é filho à esquerda
                s = x.parent.right  # s é o irmão de x
                if s.color == 'R':  # Caso 1: s é vermelho
                    s.color = 'B'  # s vira preto
                    x.parent.color = 'R'  # O pai de x vira vermelho
                    self.left_rotate(x.parent)  # Rotação à esquerda no pai de x
                    s = x.parent.right  # Atualiza s
                if s.left.color == 'B' and s.right.color == 'B':  # Caso 2: ambos os filhos de s são pretos
                    s.color = 'R'  # s vira vermelho
                    x = x.parent  # Move x para o pai
                else:
                    if s.right.color == 'B':  # Caso 3: o filho direito de s é preto
                        s.left.color = 'B'  # O filho esquerdo de s vira preto
                        s.color = 'R'  # s vira vermelho
                        self.right_rotate(s)  # Rotação à direita em s
                        s = x.parent.right  # Atualiza s
                    s.color = x.parent.color  # Caso 4: s copia a cor do pai de x
                    x.parent.color = 'B'  # O pai de x vira preto
                    s.right.color = 'B'  # O filho direito de s vira preto
                    self.left_rotate(x.parent)  # Rotação à esquerda no pai de x
                    x = self.root  # x é a raiz
            else:  # Se x é filho à direita
                s = x.parent.left  # s é o irmão de x
                if s.color == 'R':  # Caso 1: s é vermelho
                    s.color = 'B'  # s vira preto
                    x.parent.color = 'R'  # O pai de x vira vermelho
                    self.right_rotate(x.parent)  # Rotação à direita no pai de x
                    s = x.parent.left  # Atualiza s
                if s.left.color == 'B' and s.right.color == 'B':  # Caso 2: ambos os filhos de s são pretos
                    s.color = 'R'  # s vira vermelho
                    x = x.parent  # Move x para o pai
                else:
                    if s.left.color == 'B':  # Caso 3: o filho esquerdo de s é preto
                        s.right.color = 'B'  # O filho direito de s vira preto
                        s.color = 'R'  # s vira vermelho
                        self.left_rotate(s)  # Rotação à esquerda em s
                        s = x.parent.left  # Atualiza s
                    s.color = x.parent.color  # Caso 4: s copia a cor do pai de x
                    x.parent.color = 'B'  # O pai de x vira preto
                    s.left.color = 'B'  # O filho esquerdo de s vira preto
                    self.right_rotate(x.parent)  # Rotação à direita no pai de x
                    x = self.root  # x é a raiz
        x.color = 'B'  # x vira preto

##------------------------------------------------------------------------------

    def rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v  # Se u é a raiz, substitui a raiz por v
        elif u == u.parent.left:
            u.parent.left = v  # Se u é filho à esquerda, substitui por v
        else:
            u.parent.right = v  # Se u é filho à direita, substitui por v
        v.parent = u.parent  # Atualiza o pai de v

    def minimum(self, node):
        while node.left != self.TNULL:  # Encontra o nó mínimo
            node = node.left  # Desce para a esquerda
        return node  # Retorna o nó mínimo

##------------------------------------------------------------------------------

# Exemplo de uso
rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.delete_node(20)
