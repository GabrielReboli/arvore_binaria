# Arquivo: arvore_binaria.py
# Versão : 1.0
# -------------------------
# Este é um programa que implementa uma Árvore Binária de Pesquisa (BST) com
# funcionalidades de inserção, exclusão, busca e visualização gráfica. O programa
# utiliza as bibliotecas `networkx` e `matplotlib` para a visualização da árvore
# e `tkinter` para a interface gráfica.
#
# Para realizar a instalação das bibliotecas é necessario usar o instalador de 
# pacotes PIP usando o comando $ pip install "respectivas bibliotecas"
#
# Prof.: Jairo Lucas de Moraes
#

import networkx as nx
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, Frame, messagebox

# Classe: No
# Uso: no = No(valor)
# -------------------
# Esta classe representa um nó da árvore binária. Cada nó contém um valor e
# ponteiros para os nós filhos esquerdo e direito. A estrutura é fundamental
# para a construção da árvore binária de pesquisa.

class No:
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.esquerda = None  # Ponteiro para o filho esquerdo
        self.direita = None   # Ponteiro para o filho direito

# Classe: ArvoreBinaria
# Uso: arvore = ArvoreBinaria()
# -----------------------------
# Esta classe gerencia a árvore binária de pesquisa, implementando métodos para
# inserção, exclusão, busca, contagem de nós e visualização gráfica. A árvore
# mantém a propriedade de que valores menores ficam à esquerda e valores maiores
# ficam à direita.

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # Inicialmente, a árvore está vazia

    # Método: inserir
    # Uso: arvore.inserir(valor)
    # --------------------------
    # Este método insere um novo valor na árvore, mantendo a propriedade da BST.
    # Se a árvore estiver vazia, o valor é inserido como raiz. Caso contrário,
    # o método `_inserir_recursivo` é chamado para encontrar a posição correta.

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)  # Se a árvore estiver vazia, cria a raiz
        else:
            self._inserir_recursivo(self.raiz, valor)  # Chama o método recursivo

    # Método: _inserir_recursivo
    # Uso: self._inserir_recursivo(no_atual, valor)
    # ---------------------------------------------
    # Este método auxiliar percorre a árvore recursivamente para encontrar a
    # posição correta do novo valor. Valores menores são inseridos à esquerda,
    # e valores maiores são inseridos à direita. Valores duplicados são ignorados.

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:  # Se o valor for menor, vai para a esquerda
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)  # Insere à esquerda se o espaço estiver livre
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)  # Continua descendo
        elif valor > no_atual.valor:  # Se o valor for maior, vai para a direita
            if no_atual.direita is None:
                no_atual.direita = No(valor)  # Insere à direita se o espaço estiver livre
            else:
                self._inserir_recursivo(no_atual.direita, valor)  # Continua descendo
        # Se o valor for igual, não faz nada (BST não permite duplicatas)

    # Método: buscar
    # Uso: if arvore.buscar(valor): ...
    # ---------------------------------
    # Este método verifica se um valor está presente na árvore. Retorna True se
    # o valor for encontrado e False caso contrário.

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    # Método: _buscar_recursivo
    # Uso: self._buscar_recursivo(no_atual, valor)
    # --------------------------------------------
    # Este método auxiliar realiza a busca de forma recursiva. Se o valor for
    # encontrado, retorna True. Caso contrário, continua a busca nos filhos
    # esquerdo e direito.

    def _buscar_recursivo(self, no_atual, valor):
        if no_atual is None:  # Se o nó for nulo, o valor não foi encontrado
            return False
        if valor == no_atual.valor:  # Se o valor for encontrado, retorna True
            return True
        if valor < no_atual.valor:  # Se o valor for menor, busca à esquerda
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:  # Se o valor for maior, busca à direita
            return self._buscar_recursivo(no_atual.direita, valor)

    # Método: contar_nos
    # Uso: total_nos = arvore.contar_nos()
    # ------------------------------------
    # Este método conta o número total de nós na árvore. Utiliza o método
    # auxiliar `_contar_nos_recursivo` para percorrer a árvore.

    def contar_nos(self):
        return self._contar_nos_recursivo(self.raiz)

    # Método: _contar_nos_recursivo
    # Uso: self._contar_nos_recursivo(no_atual)
    # -----------------------------------------
    # Este método auxiliar conta os nós de forma recursiva. Retorna o número
    # total de nós na subárvore enraizada no nó atual.

    def _contar_nos_recursivo(self, no_atual):
        if no_atual is None:  # Se o nó for nulo, não conta
            return 0
        # Conta o nó atual e soma as contagens dos filhos esquerdo e direito
        return 1 + self._contar_nos_recursivo(no_atual.esquerda) + self._contar_nos_recursivo(no_atual.direita)

    # Método: contar_nos_nao_folhas
    # Uso: total_nao_folhas = arvore.contar_nos_nao_folhas()
    # ------------------------------------------------------
    # Este método conta o número de nós que não são folhas (nós com pelo menos
    # um filho). Utiliza o método auxiliar `_contar_nos_nao_folhas_recursivo`.

    def contar_nos_nao_folhas(self):
        return self._contar_nos_nao_folhas_recursivo(self.raiz)

    # Método: _contar_nos_nao_folhas_recursivo
    # Uso: self._contar_nos_nao_folhas_recursivo(no_atual)
    # ----------------------------------------------------
    # Este método auxiliar conta os nós não folhas de forma recursiva. Retorna
    # o número de nós não folhas na subárvore enraizada no nó atual.

    def _contar_nos_nao_folhas_recursivo(self, no_atual):
        if no_atual is None:  # Se o nó for nulo, não conta
            return 0
        nao_folhas = 0
        if no_atual.esquerda or no_atual.direita:  # Se o nó tiver pelo menos um filho
            nao_folhas = 1
        # Soma os nós não folhas das subárvores esquerda e direita
        return nao_folhas + self._contar_nos_nao_folhas_recursivo(no_atual.esquerda) + self._contar_nos_nao_folhas_recursivo(no_atual.direita)

    # Método: localizar
    # Uso: arvore.localizar(valor)
    # ----------------------------
    # Este método busca um valor na árvore e o destaca na visualização gráfica.
    # Se o valor for encontrado, ele é destacado em vermelho na árvore.

    def localizar(self, valor):
        encontrado = self.buscar(valor)  # Usa a função de busca
        if encontrado:
            print(f"Valor {valor} encontrado! Destacando na árvore...")
            self.desenhar_arvore(valor)  # Desenha a árvore com o valor destacado
        else:
            print(f"Valor {valor} NÃO encontrado na árvore!")
            self.desenhar_arvore()  # Desenha a árvore normalmente

    # Método: excluir
    # Uso: arvore.excluir(valor)
    # --------------------------
    # Este método remove um valor da árvore, mantendo-a ordenada. Utiliza o
    # método auxiliar `_excluir_recursivo` para realizar a remoção.

    def excluir(self, valor):
        self.raiz = self._excluir_recursivo(self.raiz, valor)

    # Método: _excluir_recursivo
    # Uso: self._excluir_recursivo(no_atual, valor)
    # ---------------------------------------------
    # Este método auxiliar remove o valor de forma recursiva. Três casos são
    # considerados: nó folha, nó com um filho e nó com dois filhos.

    def _excluir_recursivo(self, no_atual, valor):
        if no_atual is None:  # Se o nó for nulo, o valor não foi encontrado
            return None
        if valor < no_atual.valor:  # Se o valor for menor, busca à esquerda
            no_atual.esquerda = self._excluir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:  # Se o valor for maior, busca à direita
            no_atual.direita = self._excluir_recursivo(no_atual.direita, valor)
        else:
            # Caso 1: Nó folha
            if no_atual.esquerda is None and no_atual.direita is None:
                return None  # Remove o nó
            # Caso 2: Apenas um filho
            if no_atual.esquerda is None:
                return no_atual.direita  # Retorna o filho direito
            elif no_atual.direita is None:
                return no_atual.esquerda  # Retorna o filho esquerdo
            # Caso 3: Dois filhos
            sucessor = self._encontrar_minimo(no_atual.direita)  # Encontra o sucessor in-order
            no_atual.valor = sucessor.valor  # Copia o valor do sucessor
            no_atual.direita = self._excluir_recursivo(no_atual.direita, sucessor.valor)  # Remove o sucessor
        return no_atual  # Retorna o nó atualizado

    # Método: _encontrar_minimo
    # Uso: sucessor = self._encontrar_minimo(no)
    # ------------------------------------------
    # Este método auxiliar encontra o menor valor em uma subárvore. É utilizado
    # na exclusão de nós com dois filhos.

    def _encontrar_minimo(self, no):
        while no.esquerda is not None:  # Percorre até o nó mais à esquerda
            no = no.esquerda
        return no

    # Método: desenhar_arvore
    # Uso: arvore.desenhar_arvore(valor_procurado)
    # --------------------------------------------
    # Este método desenha a árvore graficamente utilizando as bibliotecas
    # `networkx` e `matplotlib`. Se um valor for fornecido, ele será destacado
    # em vermelho na visualização.

    def desenhar_arvore(self, valor_procurado=None):
        if self.raiz is None:  # Se a árvore estiver vazia, exibe uma mensagem
            print("A árvore está vazia!")
            return

        grafo = nx.DiGraph()  # Cria um grafo direcionado
        pos = {}
        self._adicionar_arestas(grafo, self.raiz, pos)  # Adiciona nós e arestas ao grafo
        pos = nx.get_node_attributes(grafo, 'pos')  # Obtém as posições dos nós

        # Define as cores dos nós (vermelho para o valor procurado, azul para os demais)
        cores = ["red" if no == valor_procurado else "lightblue" for no in grafo.nodes]

        plt.figure(figsize=(8, 6))  # Define o tamanho da figura
        nx.draw(grafo, pos, with_labels=True, node_size=2000, node_color=cores,
                font_size=10, font_weight="bold", edge_color="gray")  # Desenha o grafo
        plt.title("Árvore Binária de Pesquisa")  # Adiciona um título
        plt.show()  # Exibe a figura

    # Método: _adicionar_arestas
    # Uso: self._adicionar_arestas(grafo, no, pos, x, y, nivel)
    # ---------------------------------------------------------
    # Este método auxiliar adiciona nós e arestas ao grafo de forma recursiva.
    # É utilizado para construir a representação gráfica da árvore.

    def _adicionar_arestas(self, grafo, no, pos, x=0, y=0, nivel=1):
        if no is not None:
            grafo.add_node(no.valor, pos=(x, -y))  # Adiciona o nó ao grafo
            if no.esquerda is not None:
                grafo.add_edge(no.valor, no.esquerda.valor)  # Adiciona aresta para o filho esquerdo
                self._adicionar_arestas(grafo, no.esquerda, pos, x - 1 / nivel, y + 1, nivel * 2)
            if no.direita is not None:
                grafo.add_edge(no.valor, no.direita.valor)  # Adiciona aresta para o filho direito
                self._adicionar_arestas(grafo, no.direita, pos, x + 1 / nivel, y + 1, nivel * 2)

# Classe: InterfaceGrafica
# Uso: app = InterfaceGrafica(root)
# ---------------------------------
# Esta classe implementa a interface gráfica do programa utilizando a biblioteca
# `tkinter`. Ela permite que o usuário interaja com a árvore de forma intuitiva,
# realizando operações como inserção, exclusão, busca e visualização.

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Árvore Binária de Pesquisa")
        self.arvore = ArvoreBinaria()

        # Frame para entrada de dados
        frame_entrada = Frame(root)
        frame_entrada.pack(pady=10)

        Label(frame_entrada, text="Valor:").grid(row=0, column=0, padx=5)
        self.entrada_valor = Entry(frame_entrada, width=10)
        self.entrada_valor.grid(row=0, column=1, padx=5)

        Button(frame_entrada, text="Inserir", command=self.inserir).grid(row=0, column=2, padx=5)
        Button(frame_entrada, text="Excluir", command=self.excluir).grid(row=0, column=3, padx=5)
        Button(frame_entrada, text="Buscar", command=self.buscar).grid(row=0, column=4, padx=5)
        Button(frame_entrada, text="Contar Nós", command=self.contar_nos).grid(row=0, column=5, padx=5)
        Button(frame_entrada, text="Contar Nós Não Folhas", command=self.contar_nos_nao_folhas).grid(row=0, column=6, padx=5)

        # Frame para exibição de informações
        frame_info = Frame(root)
        frame_info.pack(pady=10)

        self.texto_info = Text(frame_info, height=15, width=70, font=("Arial", 12))
        self.texto_info.pack(side="left", fill="y")



