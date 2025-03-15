# pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt

class No:
    def __init__(self, valor):
        self.valor = valor  # Define o valor do nó
        self.esquerda = None  # O nó começa sem filhos
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # Inicialmente, a árvore está vazia

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)  # Se a árvore estiver vazia, cria a raiz
        else:
            self._inserir_recursivo(self.raiz, valor)  # Chama método auxiliar recursivo

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)  # Insere à esquerda se o espaço estiver livre
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)  # Continua descendo
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)  # Insere à direita se o espaço estiver livre
            else:
                self._inserir_recursivo(no_atual.direita, valor)  # Continua descendo
        # Se for igual, não faz nada (BST não permite duplicatas)

    
    def buscar(self, valor):
        """Busca um valor na árvore e retorna True se encontrado, False caso contrário."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no_atual, valor):
        """Função recursiva para buscar um valor na árvore."""
        if no_atual is None:
            return False  # Não encontrou o valor

        if valor == no_atual.valor:
            return True  # Encontrou o valor

        if valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)  # Busca à esquerda
        else:
            return self._buscar_recursivo(no_atual.direita, valor)  # Busca à direita



    def _adicionar_arestas(self, grafo, no, pos, x=0, y=0, nivel=1):
        """Adiciona os nós e arestas ao grafo recursivamente."""
        if no is not None:
            grafo.add_node(no.valor, pos=(x, -y))  # Adiciona nó com posição
            if no.esquerda is not None:
                grafo.add_edge(no.valor, no.esquerda.valor)  # Conecta pai -> filho esquerdo
                self._adicionar_arestas(grafo, no.esquerda, pos, x - 1 / nivel, y + 1, nivel * 2)
            if no.direita is not None:
                grafo.add_edge(no.valor, no.direita.valor)  # Conecta pai -> filho direito
                self._adicionar_arestas(grafo, no.direita, pos, x + 1 / nivel, y + 1, nivel * 2)

    def desenhar_arvore(self, valor_procurado=None):
        """Desenha a árvore binária e destaca um nó se estiver sendo buscado."""
        if self.raiz is None:
            print("A árvore está vazia!")
            return

        grafo = nx.DiGraph()
        pos = {}
        self._adicionar_arestas(grafo, self.raiz, pos)
        pos = nx.get_node_attributes(grafo, 'pos')  # Obtém posições dos nós

        # Definir cores: azul para todos, vermelho para o nó buscado
        cores = ["red" if no == valor_procurado else "lightblue" for no in grafo.nodes]

        plt.figure(figsize=(8, 6))
        nx.draw(grafo, pos, with_labels=True, node_size=2000, node_color=cores,
            font_size=10, font_weight="bold", edge_color="gray")
        plt.title("Árvore Binária de Pesquisa")
        plt.show()

    def contar_nos(self):
        """Contar o número de nós da árvore."""
        return self._contar_nos_recursivo(self.raiz)

    def _contar_nos_recursivo(self, no_atual):
        """Função recursiva para contar os nós na árvore."""
        if no_atual is None:
            return 0  # Se o nó não existe, não conta

        # Conta o nó atual e soma as contagens dos filhos esquerdo e direito
        return 1 + self._contar_nos_recursivo(no_atual.esquerda) + self._contar_nos_recursivo(no_atual.direita)

    def contar_nos_nao_folhas(self):
        """Conta o número de nós não-folhas na árvore."""
        _, nos_nao_folhas = self._contar_nos_e_nos_nao_folhas(self.raiz)
        return nos_nao_folhas
    
    def _contar_nos_e_nos_nao_folhas(self, no_atual):
        """Função recursiva que conta apenas os nós não-folhas."""
        if no_atual is None:
            return 0, 0  # Sem nó, não conta nada

        # Contagem das subárvores esquerda e direita
        nao_folhas_esquerda = self._contar_nos_e_nos_nao_folhas(no_atual.esquerda)[1]
        nao_folhas_direita = self._contar_nos_e_nos_nao_folhas(no_atual.direita)[1]

        # Verificar se o nó atual é não-folha (tem pelo menos um filho)
        nos_nao_folhas = 0
        if no_atual.esquerda or no_atual.direita:  # Verifica ambos os lados
            nos_nao_folhas = 1

        # Soma os nós não-folhas das subárvores
        nos_nao_folhas += nao_folhas_esquerda + nao_folhas_direita

        return 0, nos_nao_folhas  # Não precisamos contar o total de nós, só os não-folhas


    def destacar_busca(self, valor):
        """Procura um valor e destaca ele na árvore, se encontrado."""
        encontrado = self.buscar(valor)  # Usa a função de busca já existente
        if encontrado:
            print(f"Valor {valor} encontrado! Destacando na árvore...")
            self.desenhar_arvore(valor)
        else:
            print(f"Valor {valor} NÃO encontrado na árvore!")
            self.desenhar_arvore()  # Mostra a árvore normal



# Criando a árvore binária e inserindo valores
arvore = ArvoreBinaria()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

# Testando a contagem de nós
total_nos = arvore.contar_nos()
print(f"Total de nós na árvore: {total_nos}")

# Testando a contagem de nós não-folhas
total_nao_folhas = arvore.contar_nos_nao_folhas()
print(f"Total de nós não-folhas: {total_nao_folhas}")





