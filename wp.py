import networkx as nx
import matplotlib.pyplot as plt
import itertools
import time

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
    
    cor_atual = 0 #começa no 0 para ser melhor a contagem
    
    #Faz a varredura do vetor
    for v in vertices_ordenados:
        if mapa_cores[v] == -1:# vertice incolor
            mapa_cores[v] = cor_atual#se estiver incolor pinta com a cor do vetor da paleta
            
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

#função que calcular o X(G), ou seja o menor número de cores uilizadas possiveis
def numero_cromatico_itertools(grafo):
    vertices = list(grafo.keys())
    n = len(vertices)

    # Converte grafo p/ índice ou seja inteiro
    idx = {v: i for i, v in enumerate(vertices)}

    # Matriz de adjacência indexada
    adj = [[] for _ in range(n)]
    for v in vertices:
        for viz in grafo[v]:
            adj[idx[v]].append(idx[viz])

    # Tentar de k=1 até k=n cores,para ver menor número de cores possiveis
    for k in range(1, n + 1):
        # Gera todas as colorações possíveis com k cores
        for coloracao in itertools.product(range(k), repeat=n):
            valido = True
            # Verifica se coloração é válida
            for v in range(n):
                cor_v = coloracao[v]
                for viz in adj[v]:
                    if coloracao[viz] == cor_v:
                        valido = False
                        break
                if not valido:
                    break
            if valido:
                return k  # achou o χ(G), menor número de cores possiveis
    return n


# ------------------------------------------------------------
# 3. FATOR DE APROXIMAÇÃO ρ
# ------------------------------------------------------------
def calcular_fator_aproximacao(grafo):
    cores_wp = welsh_powell(grafo)
    num_wp = len(set(cores_wp.values()))

    num_otimo = numero_cromatico_itertools(grafo)

    rho = num_wp / num_otimo
    return rho, num_wp, num_otimo, cores_wp



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

#BENCHMARK SIMPLES

def fatorAproximacao(grafo):
    print("\n--- Fator de Aproximação ---")

    t0 = time.time()
    _, num_wp, _, _ = calcular_fator_aproximacao(grafo)
    t1 = time.time()

    t_wp = t1 - t0

    print(f"Cores Welsh-Powell = {num_wp}")
    print(f"Tempo total (WP + χ(G) exato) = {t_wp:.6f} segundos")
    print("------------------------\n")




#EXECUÇÃO
indices_cores = welsh_powell(grafo) 
fatorAproximacao(grafo)



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
#plt.savefig("welshPowellString.png")
plt.savefig("welshPowellInt.png")
#Mostra em uma iagem, sem salvar o arquivo, o grafo
#plt.show()