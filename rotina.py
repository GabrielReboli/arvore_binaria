# pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, Frame, messagebox

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
        return self._contar_nos_nao_folhas_recursivo(self.raiz)

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

    def localizar(self, valor):
        """Procura um valor e destaca ele na árvore, se encontrado."""
        encontrado = self.buscar(valor)  # Usa a função de busca já existente
        if encontrado:
            print(f"Valor {valor} encontrado! Destacando na árvore...")
            self.desenhar_arvore(valor)
        else:
            print(f"Valor {valor} NÃO encontrado na árvore!")
            self.desenhar_arvore()  # Mostra a árvore normal

    def excluir(self, valor):
        """Remove um nó da árvore mantendo-a ordenada."""
        self.raiz = self._excluir_recursivo(self.raiz, valor)

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

    def _encontrar_minimo(self, no):
        """Encontra o menor valor em uma subárvore."""
        while no.esquerda is not None:
            no = no.esquerda
        return no
    

# Interface Gráfica
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


