import networkx as nx
import matplotlib.pyplot as plt

# ==========================================================
# FUNÇÃO UNIVERSAL (Funciona para INT e STRING)
# ==========================================================
def coloracao_universal(grafo_dict):
    colors = {} 
    
    # Ordenamos as chaves para garantir que o resultado não mude a cada execução
    nodos = sorted(list(grafo_dict.keys()), key=lambda x: str(x))
    
    for u in nodos:
        # Pega vizinhos
        vizinhos = grafo_dict[u]
        
        # O segredo da universalidade:
        # Verificamos "if v in colors" (funciona pra tudo)
        forbidden = {colors[v] for v in vizinhos if v in colors}
        
        cor = 0
        while cor in forbidden:
            cor += 1
            
        colors[u] = cor
    
    return colors

# ==========================================================
# TESTE 1: Cidades (Strings)
# ==========================================================
#grafo = {
 #   "RS": ["SC"],
  #  "SC": ["RS", "PR"],
   # "PR": ["SC", "SP", "MS"],
   # "SP": ["PR", "MS", "MG", "RJ"],
   # "MS": ["PR", "SP", "MG", "GO", "MT"],
   # "RJ": ["SP", "MG", "ES"],
   # "MG": ["SP", "RJ", "ES", "BA", "GO", "MS"],
   # "ES": ["RJ", "MG", "BA"],
   # "GO": ["MS", "MT", "BA", "MG"],
   # "MT": ["MS", "GO"],
   # "BA": ["MG", "ES", "GO"]
#}

# ==========================================================
# TESTE 2: Números Inteiros (Formatados como Dicionário)
# ==========================================================
# Note: Em vez de [], usamos {} e definimos a chave explicitamente
grafo = {
    0: [2, 3, 1, 4],       # 0
    1: [0, 3, 2, 4],       # 1
    2: [3, 1, 0, 8],       # 2
    3: [2, 0, 1, 6, 7],    # 3
    4: [5, 0, 1],          # 4
    5: [4, 9, 8, 10],      # 5
    6: [7, 3, 10],         # 6
    7: [9, 10, 3, 8, 6],   # 7
    8: [5, 2, 9, 7],       # 8
    9: [7, 5, 8, 10],      # 9
    10: [6, 9, 7, 5]        # 10
}

# ==========================================================
# EXECUÇÃO E PLOTAGEM (Mesma função para os dois!)
# ==========================================================

# Escolha qual grafo quer testar aqui:
grafo_ativo = grafo  # <--- Troque por grafo_numeros para testar
titulo = "Grafo de Cidades"

# 1. Roda a função universal
cores = coloracao_universal(grafo_ativo)

# 2. Configura visualização
G = nx.Graph()
for u, vizinhos in grafo_ativo.items():
    for v in vizinhos:
        G.add_edge(u, v)

palette = ["pink", "lightblue", "lightgreen", "gold", "blue", 
    "red", "darkgreen", "purple", "orange", "teal", 
    "gray", "cyan", "magenta", "lime", "brown",
    "olive", "navy", "maroon", "orchid", "salmon"]

# 3. Lógica de Cores Universal
ordem_dos_nos = list(G.nodes())
node_colors = [palette[cores[no] % len(palette)] for no in ordem_dos_nos]
#[palette[cores[no] % len(palette)] for no in ordem_dos_nos]

# 4. Desenha
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G,
    pos,
    with_labels=True,
    # AQUI ESTÁ A MÁGICA:
    # Como node_color foi criado baseado em G.nodes(), tudo se alinha perfeitamente
    node_color=node_colors, 
    node_size=1000,
    font_size=12,
    font_weight="bold",
    edge_color="gray",
    width=1.5
)
plt.title(titulo)
plt.show()
plt.savefig("gulosoUniversal.png")
#plt.savefig("gulosoUniversalString.png")
print("Cores atribuídas:", cores)