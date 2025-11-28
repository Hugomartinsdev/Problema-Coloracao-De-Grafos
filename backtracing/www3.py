import networkx as nx
import matplotlib.pyplot as plt

#Paleta de cor
palette = [
   "pink", "lightblue", "lightgreen", "gold", "blue", 
    "red", "darkgreen", "purple", "orange", "teal", 
    "gray", "cyan", "magenta", "lime", "brown",
    "olive", "navy", "maroon", "orchid", "salmon"
]


def welsh_powell(grafo):
    # Ordena índices pelo grau decrescente, caracteristica do weesh_Powell, e procura o vertice com maior grao,mais vizinhos
    vertices_ordenados = sorted(grafo.keys(), key=lambda v: len(grafo[v]), reverse=True)
    
    # 2. Inicializa o mapa de cores como um DICIONÁRIO
    mapa_cores = {v: -1 for v in grafo.keys()}
    
    cor_atual = 0 
    
    for v in vertices_ordenados:
        if mapa_cores[v] == -1:
            mapa_cores[v] = cor_atual
            
            #Procura vertices que não são vizinhos para pintar ele com a mesma cor do loop atual
            for u in vertices_ordenados:
                if mapa_cores[u] == -1:
                    # A lógica de vizinhos continua igual
                    # Verifica se NENHUM vizinho de 'u' tem a cor atual
                    if all(mapa_cores[viz] != cor_atual for viz in grafo[u]):
                        mapa_cores[u] = cor_atual
            # Só incrementa a cor depois de pintar todos possíveis com a atual
            cor_atual += 1
            
    return mapa_cores

#grafo = {
#    "RS": ["SC"],
#    "SC": ["RS", "PR"],
#    "PR": ["SC", "SP", "MS"],
#    "SP": ["PR", "MS", "MG", "RJ"],
#    "MS": ["PR", "SP", "MG", "GO", "MT"],
#    "RJ": ["SP", "MG", "ES"],
#    "MG": ["SP", "RJ", "ES", "BA", "GO", "MS"],
#    "ES": ["RJ", "MG", "BA"],
#    "GO": ["MS", "MT", "BA", "MG"],
#    "MT": ["MS", "GO"],
#    "BA": ["MG", "ES", "GO"]
#}

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
    10: [6, 9, 7, 5]        #
}

#EXECUÇÃO
indices_cores = welsh_powell(grafo) 
print("-" * 50)
print(f"Nó 0  -> Cor Numérica: {indices_cores[0]} | Cor Visual: {palette[indices_cores[0]]}")
print(f"Nó 1 -> Cor Numérica: {indices_cores[1]} | Cor Visual: {palette[indices_cores[1]]}")
print(f"Nó 2 -> Cor Numérica: {indices_cores[2]} | Cor Visual: {palette[indices_cores[2]]}")
print(f"Nó 3 -> Cor Numérica: {indices_cores[3]} | Cor Visual: {palette[indices_cores[3]]}")
print(f"Nó 4  -> Cor Numérica: {indices_cores[4]} | Cor Visual: {palette[indices_cores[4]]}")
print(f"Nó 5 -> Cor Numérica: {indices_cores[5]} | Cor Visual: {palette[indices_cores[5]]}")
print(f"Nó 6  -> Cor Numérica: {indices_cores[6]} | Cor Visual: {palette[indices_cores[6]]}")
print(f"Nó 7 -> Cor Numérica: {indices_cores[7]} | Cor Visual: {palette[indices_cores[7]]}")
print(f"Nó 8  -> Cor Numérica: {indices_cores[8]} | Cor Visual: {palette[indices_cores[8]]}")
print(f"Nó 9  -> Cor Numérica: {indices_cores[9]} | Cor Visual: {palette[indices_cores[9]]}")
print(f"Nó 10 -> Cor Numérica: {indices_cores[10]} | Cor Visual: {palette[indices_cores[10]]}")
print("-" * 50)

#MONTAGEM DO GRAFICO
G = nx.Graph(grafo) 


mapa_cores_visualizacao = []

# retorna "A", "B", "C"
for no in G.nodes():
    # Pegamos o ID da cor usando o NOME do nó no nosso resultado
    id_cor = indices_cores[no]
    
    # Pega a cor real na paleta
    # esse %len(palette) é usado para caso  o algoritmo use mais cor do que o vetor palette possui, faz a cor "dar a volta". por exemplo A cor 3 vira a cor 0 A cor 4 vira a cor 1. e asim por diante
    cor_real = palette[id_cor % len(palette)]

    #aqui faz o append para plotar o grafico
    mapa_cores_visualizacao.append(cor_real)

#Monta o formato do desenho do grafo, a seed faz com que o formaato do desenho fique fixo
pos = nx.spring_layout(G, seed=42)

#Função para criar o grafico
nx.draw(
    G, 
    pos, 
    with_labels=True, 
    node_color=mapa_cores_visualizacao, 
    node_size=1000,
    font_weight='bold', 
    font_color='white'
)

#salva o grafo em formato de png 
plt.savefig("welshPowellString.png")
plt.savefig("welshPowellInt.png")
#Mostra em uma iagem, sem salvar o arquivo, o grafo
plt.show()