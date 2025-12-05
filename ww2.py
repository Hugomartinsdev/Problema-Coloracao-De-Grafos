import networkx as nx
import matplotlib.pyplot as plt


palette = [
   "pink", "lightblue", "lightgreen", "gold", "blue", 
    "red", "darkgreen", "purple", "orange", "teal", 
    "gray", "cyan", "magenta", "lime", "brown",
    "olive", "navy", "maroon", "orchid", "salmon"
]

# --- 2. ALGORITMO WELSH-POWELL ---
def welsh_powell(grafo):
    n = len(grafo)
    # Ordena índices pelo grau decrescente
    vertices_ordenados = sorted(range(n), key=lambda v: len(grafo[v]), reverse=True)
    
    cores_indices = [-1] * n
    cor_atual = 0 #só para ser mais facil a contagem
    
    for v in vertices_ordenados:
        if cores_indices[v] == -1:
            cores_indices[v] = cor_atual
            
            for u in vertices_ordenados:
                if cores_indices[u] == -1:
                    # Verifica vizinhos
                    if all(cores_indices[viz] != cor_atual for viz in grafo[u]):
                        cores_indices[u] = cor_atual
            
            # Só incrementa a cor depois de pintar todos possíveis com a atual
            cor_atual += 1
            
    return cores_indices

# --- 3. DADOS DE ENTRADA ---
grafo_lista = [
    [2, 3, 1, 4],       # 0
    [0, 3, 2, 4],       # 1
    [3, 1, 0, 8],       # 2
    [2, 0, 1, 6, 7],    # 3
    [5, 0, 1],          # 4
    [4, 9, 8, 10],      # 5
    [7, 3, 10],         # 6
    [9, 10, 3, 8, 6],   # 7
    [5, 2, 9, 7],       # 8
    [7, 5, 8, 10],      # 9
    [6, 9, 7, 5]        # 10
]

# --- 4. EXECUÇÃO ---
# Retorna algo como [0, 1, 0, 2...] (índices das cores)
indices_cores = welsh_powell(grafo_lista) 

# --- 5. MONTAGEM DO GRAFICO E MAPEAMENTO BLINDADO ---
G = nx.Graph()

# Adiciona nós e arestas
for i, vizinhos in enumerate(grafo_lista):
    G.add_node(i)
    for vizinho in vizinhos:
        G.add_edge(i, vizinho)

# --- A CORREÇÃO DO ERRO ---
# O nx.draw pinta os nós na ordem de G.nodes(). 
# Precisamos criar a lista de cores NESSA MESMA ORDEM.

mapa_cores_final = []

for no in G.nodes():
    # 1. Qual o índice da cor que o Welsh-Powell deu para este nó?
    id_cor = indices_cores[no]
    
    # 2. Pega a cor correspondente no SEU vetor pré-pronto
    # O operador % garante que não dê erro se faltar cor (ele repete)
    cor_real = palette[id_cor % len(palette)]
    
    mapa_cores_final.append(cor_real)

# --- 6. DESENHO ---
pos = nx.spring_layout(G, seed=42) # Layout fixo

nx.draw(
    G, 
    pos, 
    with_labels=True, 
    node_color=mapa_cores_final, # Aqui entra a lista sincronizada
    node_size=800, 
    font_color='black', # Mudei para preto para ler melhor no amarelo/ciano
    font_weight='bold',
    edge_color='gray'
)
plt.savefig("welshPowell.png")
plt.show()