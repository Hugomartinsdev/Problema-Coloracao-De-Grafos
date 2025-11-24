import networkx as nx
import matplotlib.pyplot as plt

#criação do grafo/Matriz de adjacencia
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

#Teste com letra, para mostrar que o codigo serve tanto para int tanto para string
#grafo = {
#    "RS": ["SC"],
#    "SC": ["RS", "PR"],
#    "PR": ["SC", "SP", "MS"],
#    "SP": ["PR", "MS", "MG", "RJ"],
#    "MS": ["PR", "SP", "MG", "GO", "MT"],
#    "RJ": ["SP", "MG", "ES"],
#    "MG": ["SP", "RJ", "ES", "BA", "GO", "MS"],
#    "ES": ["RJ", "MG", "BA"],
#    "GO": ["MS", "MT", "BA", "MG", "TO"],
#    "MT": ["MS", "GO", "TO", "RO"],
#    "BA": ["MG", "ES", "GO", "TO", "SE"],
#    "ILHA_SOLITARIA": []
#}

# ==========================================
# 2. Algoritmo de Coloração Gulosa
# ==========================================
def greedy_coloring(adj):
    n = len(adj)
    colors = [-1] * n
    
    for v in range(n):
        # Descobre quais cores os vizinhos já estão usando
        forbidden = {colors[u] for u in adj[v] if colors[u] != -1}
        
        # Encontra a menor cor numérica (0, 1, 2...) disponível
        cor = 0
        while cor in forbidden:
            cor += 1
            
        colors[v] = cor
    
    return colors, max(colors) + 1

# Executa o algoritmo
colors_numericos, k = greedy_coloring(grafo)
print(f"Algoritmo concluído. Total de cores usadas: {k}")


# ==========================================
# 3. Configuração Visual (Paleta)
# ==========================================
# Paleta de 20 cores
palette = [
    "pink", "lightblue", "lightgreen", "gold", "blue", 
    "red", "darkgreen", "purple", "orange", "teal", 
    "gray", "cyan", "magenta", "lime", "brown",
    "olive", "navy", "maroon", "orchid", "salmon"
]

print("-" * 50)
print("Validação dos Vizinhos Problemáticos (5 e 10):")
print(f"Nó 0  -> Cor Numérica: {colors_numericos[0]} | Cor Visual: {palette[colors_numericos[0]]}")
print(f"Nó 1 -> Cor Numérica: {colors_numericos[1]} | Cor Visual: {palette[colors_numericos[1]]}")
print(f"Nó 2 -> Cor Numérica: {colors_numericos[2]} | Cor Visual: {palette[colors_numericos[2]]}")
print(f"Nó 3 -> Cor Numérica: {colors_numericos[3]} | Cor Visual: {palette[colors_numericos[3]]}")
print(f"Nó 4  -> Cor Numérica: {colors_numericos[4]} | Cor Visual: {palette[colors_numericos[4]]}")
print(f"Nó 5 -> Cor Numérica: {colors_numericos[5]} | Cor Visual: {palette[colors_numericos[5]]}")
print(f"Nó 6  -> Cor Numérica: {colors_numericos[6]} | Cor Visual: {palette[colors_numericos[6]]}")
print(f"Nó 7 -> Cor Numérica: {colors_numericos[7]} | Cor Visual: {palette[colors_numericos[7]]}")
print(f"Nó 8  -> Cor Numérica: {colors_numericos[8]} | Cor Visual: {palette[colors_numericos[8]]}")
print(f"Nó 9  -> Cor Numérica: {colors_numericos[9]} | Cor Visual: {palette[colors_numericos[9]]}")
print(f"Nó 10 -> Cor Numérica: {colors_numericos[10]} | Cor Visual: {palette[colors_numericos[10]]}")
print("-" * 50)


# 4. Construção do Grafo NetworkX
G = nx.Graph()

# Adiciona os nós explicitamente (boa prática)
for i in range(len(grafo)):
    G.add_node(i)

# Adiciona as arestas
for v, vizinhos in enumerate(grafo):
    for u in vizinhos:
        if v < u: # Evita duplicar arestas em grafos não direcionados
            G.add_edge(v, u)


ordem_dos_nos_no_nx = list(G.nodes())

# palette[...] -> transforma o número na cor visual (ex: 'gold')
node_colors_ordenado = [palette[colors_numericos[no] % len(palette)] for no in ordem_dos_nos_no_nx]


# 6. Plotagem

pos = nx.spring_layout(G, seed=42) # Seed fixa para o desenho não mudar a cada execução

nx.draw(
    G,
    pos,
    with_labels=True,
    # AQUI ESTÁ A MÁGICA:
    # Como node_color foi criado baseado em G.nodes(), tudo se alinha perfeitamente
    node_color=node_colors_ordenado, 
    node_size=1000,
    font_size=12,
    font_weight="bold",
    edge_color="gray",
    width=1.5
)



# Salva e mostra
plt.savefig("guloso.png")
plt.show()