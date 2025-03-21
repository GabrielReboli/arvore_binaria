# Arquivo: rotina.py
# Versão : 1.1
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
        self.valor = valor  # Define o valor do nó
        self.esquerda = None  # O nó começa sem filhos
        self.direita = None

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
            self._inserir_recursivo(self.raiz, valor)  # Chama método auxiliar recursivo

    # Método: _inserir_recursivo
    # Uso: self._inserir_recursivo(no_atual, valor)
    # ---------------------------------------------
    # Este método auxiliar percorre a árvore recursivamente para encontrar a
    # posição correta do novo valor. Valores menores são inseridos à esquerda,
    # e valores maiores são inseridos à direita. Valores duplicados são ignorados.
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

    # Método: buscar
    # Uso: if arvore.buscar(valor): ...
    # ---------------------------------
    # Este método verifica se um valor está presente na árvore. Retorna True se
    def buscar(self, valor):
        """Busca um valor na árvore e retorna True se encontrado, False caso contrário."""
        return self._buscar_recursivo(self.raiz, valor)

    # Método: _buscar_recursivo
    # Uso: self._buscar_recursivo(no_atual, valor)
    # --------------------------------------------
    # Este método auxiliar realiza a busca de forma recursiva. Se o valor for
    # encontrado, retorna True. Caso contrário, continua a busca nos filhos
    # esquerdo e direito.
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


    # Método: _adicionar_arestas
    # Uso: self._adicionar_arestas(grafo, no, pos, x, y, nivel)
    # ---------------------------------------------------------
    # Este método auxiliar adiciona nós e arestas ao grafo de forma recursiva.
    # É utilizado para construir a representação gráfica da árvore.
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

    # Método: desenhar_arvore
    # Uso: arvore.desenhar_arvore(valor_procurado)
    # --------------------------------------------
    # Este método desenha a árvore graficamente utilizando as bibliotecas
    # `networkx` e `matplotlib`. Se um valor for fornecido, ele será destacado
    # em vermelho na visualização.
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

    # Método: contar_nos
    # Uso: total_nos = arvore.contar_nos()
    # ------------------------------------
    # Este método conta o número total de nós na árvore. Utiliza o método
    # auxiliar `_contar_nos_recursivo` para percorrer a árvore.
    def contar_nos(self):
        """Contar o número de nós da árvore."""
        return self._contar_nos_recursivo(self.raiz)

    # Método: _contar_nos_recursivo
    # Uso: self._contar_nos_recursivo(no_atual)
    # -----------------------------------------
    # Este método auxiliar conta os nós de forma recursiva. Retorna o número
    # total de nós na subárvore enraizada no nó atual.
    def _contar_nos_recursivo(self, no_atual):
        """Função recursiva para contar os nós na árvore."""
        if no_atual is None:
            return 0  # Se o nó não existe, não conta

        # Conta o nó atual e soma as contagens dos filhos esquerdo e direito
        return 1 + self._contar_nos_recursivo(no_atual.esquerda) + self._contar_nos_recursivo(no_atual.direita)

    # Método: contar_nos_nao_folhas
    # Uso: total_nao_folhas = arvore.contar_nos_nao_folhas()
    # ------------------------------------------------------
    # Este método conta o número de nós que não são folhas (nós com pelo menos
    # um filho). Utiliza o método auxiliar `_contar_nos_nao_folhas_recursivo`.
    def contar_nos_nao_folhas(self):
        """Conta o número de nós não-folhas na árvore."""
        return self._contar_nos_nao_folhas_recursivo(self.raiz)

    # Método: _contar_nos_nao_folhas_recursivo
    # Uso: self._contar_nos_nao_folhas_recursivo(no_atual)
    # ----------------------------------------------------
    # Este método auxiliar conta os nós não folhas de forma recursiva. Retorna
    # o número de nós não folhas na subárvore enraizada no nó atual.
    def _contar_nos_nao_folhas_recursivo(self, no_atual):
        """Função recursiva para contar os nós não-folhas."""
        if no_atual is None:
            return 0  # Se o nó não existe, não conta

        # Conta o nó atual se ele não for folha (tem pelo menos um filho)
        nao_folhas = 0
        if no_atual.esquerda or no_atual.direita:
            nao_folhas = 1

        # Conta os nós não-folhas das subárvores esquerda e direita
        return nao_folhas + self._contar_nos_nao_folhas_recursivo(no_atual.esquerda) + self._contar_nos_nao_folhas_recursivo(no_atual.direita)

    # Método: localizar
    # Uso: arvore.localizar(valor)
    # ----------------------------
    # Este método busca um valor na árvore e o destaca na visualização gráfica.
    # Se o valor for encontrado, ele é destacado em vermelho na árvore.
    def localizar(self, valor):
        """Procura um valor e destaca ele na árvore, se encontrado."""
        encontrado = self.buscar(valor)  # Usa a função de busca já existente
        if encontrado:
            print(f"Valor {valor} encontrado! Destacando na árvore...")
            self.desenhar_arvore(valor)
        else:
            print(f"Valor {valor} NÃO encontrado na árvore!")
            self.desenhar_arvore()  # Mostra a árvore normal

    # Método: excluir
    # Uso: arvore.excluir(valor)
    # --------------------------
    # Este método remove um valor da árvore, mantendo-a ordenada. Utiliza o
    # método auxiliar `_excluir_recursivo` para realizar a remoção.
    def excluir(self, valor):
        """Remove um nó da árvore mantendo-a ordenada."""
        self.raiz = self._excluir_recursivo(self.raiz, valor)

    # Método: _excluir_recursivo
    # Uso: self._excluir_recursivo(no_atual, valor)
    # ---------------------------------------------
    # Este método auxiliar remove o valor de forma recursiva. Três casos são
    # considerados: nó folha, nó com um filho e nó com dois filhos.
    def _excluir_recursivo(self, no_atual, valor):
        """Função recursiva para remover um nó da árvore."""
        if no_atual is None:
            return None  # Valor não encontrado, nada a remover

        if valor < no_atual.valor:
            no_atual.esquerda = self._excluir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
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
            sucessor = self._encontrar_minimo(no_atual.direita)
            no_atual.valor = sucessor.valor  # Copia o valor do sucessor
            no_atual.direita = self._excluir_recursivo(no_atual.direita, sucessor.valor)  # Remove o sucessor

        return no_atual  # Retorna o nó atualizado

    # Método: _encontrar_minimo
    # Uso: sucessor = self._encontrar_minimo(no)
    # ------------------------------------------
    # Este método auxiliar encontra o menor valor em uma subárvore. É utilizado
    # na exclusão de nós com dois filhos.
    def _encontrar_minimo(self, no):
        """Encontra o menor valor em uma subárvore."""
        while no.esquerda is not None:
            no = no.esquerda
        return no
    

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

        # Definir tamanho inicial da janela
        self.root.geometry("952x532")  # Largura x Altura

        # Frame para entrada de dados
        frame_entrada = Frame(root)
        frame_entrada.pack(pady=10)

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

        self.texto_info = Text(frame_info, height=20, width=108, font=("Arial", 12, "bold"))
        self.texto_info.pack(side="left", fill="y")

        scrollbar = Scrollbar(frame_info, command=self.texto_info.yview)
        scrollbar.pack(side="right", fill="y")
        self.texto_info.config(yscrollcommand=scrollbar.set)

        # Botão para desenhar a árvore
        Button(root, text="Desenhar Árvore", command=self.desenhar_arvore).pack(pady=10)

    def contar_nos(self):
        self.atualizar_info(f"Total de nós: {self.arvore.contar_nos()}.")

    def contar_nos_nao_folhas(self):
        self.atualizar_info(f"Total de nós não folhas: {self.arvore.contar_nos_nao_folhas()}.")

    def inserir(self):
        valor = self.entrada_valor.get()
        if valor:
            try:
                valor = int(valor)
                self.arvore.inserir(valor)
                self.atualizar_info(f"Valor {valor} inserido com sucesso!")
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um número válido.")
        else:
            messagebox.showerror("Erro", "Por favor, insira um valor.")

    def excluir(self):
        valor = self.entrada_valor.get()
        if valor:
            try:
                valor = int(valor)
                self.arvore.excluir(valor)
                self.atualizar_info(f"Valor {valor} excluído com sucesso!")
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um número válido.")
        else:
            messagebox.showerror("Erro", "Por favor, insira um valor.")

    def buscar(self):
        valor = self.entrada_valor.get()
        if valor:
            try:
                valor = int(valor)
                self.arvore.localizar(valor)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um número válido.")
        else:
            messagebox.showerror("Erro", "Por favor, insira um valor.")

    def desenhar_arvore(self):
        self.arvore.desenhar_arvore()

    def atualizar_info(self, mensagem):
        self.texto_info.insert("end", mensagem + "\n")
        self.texto_info.see("end")

# Inicialização da interface gráfica
if __name__ == "__main__":
    root = Tk()
    app = InterfaceGrafica(root)
    root.mainloop()


