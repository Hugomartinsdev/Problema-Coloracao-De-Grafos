import matplotlib.pyplot as plt
import networkx as nx


# ----------------------------
# FUNÇÕES DE COLORAÇÃO (BACKTRACKING)
# ----------------------------

def pode_colorir(grafo, cor_atual, cores, vertice):
    for vizinho in grafo[vertice]:
        if cores[vizinho] == cor_atual:
            return False
    return True


def colorir_recursivo(grafo, max_cores, cores, v=0):
    if v == len(grafo):
        return True

    for cor in range(1, max_cores + 1):
        if pode_colorir(grafo, cor, cores, v):
            cores[v] = cor

            if colorir_recursivo(grafo, max_cores, cores, v + 1):
                return True

            cores[v] = 0  # backtracking

    return False


def colorir_escalavel(grafo):
    n = len(grafo)
    cores = [0] * n

    for max_cores in range(1, n + 1):
        print(f"Tentando com {max_cores} cores...")

        cores = [0] * n
        if colorir_recursivo(grafo, max_cores, cores):
            return cores, max_cores

    return None, None


# ----------------------------
# EXEMPLO DE GRAFO
# ----------------------------

grafo = [
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

cores, usadas = colorir_escalavel(grafo)
print("Cores:", cores)
print("Número de cores usadas:", usadas)


# ----------------------------
# DESENHAR GRAFO COM NETWORKX
# ----------------------------

# Cria grafo NetworkX
G = nx.Graph()

# Adiciona vértices
G.add_nodes_from(range(len(grafo)))

# Adiciona arestas
for v in range(len(grafo)):
    for viz in grafo[v]:
        if v < viz:  # evita duplicar arestas
            G.add_edge(v, viz)

# Gera posições (layout bonito)
pos = nx.spring_layout(G, seed=42)

# Mapear cada número de cor para uma cor real do Matplotlib
color_map = plt.cm.get_cmap('tab10', usadas)
node_colors = [color_map(c - 1) for c in cores]  # cores começam em 1

# Desenhar
plt.figure(figsize=(6, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=1000,
    font_size=12,
    font_weight='bold'
)

plt.title(f"Grafo colorido com {usadas} cores")
plt.show()
