def welsh_powell(grafo):
    n = len(grafo)

    # 1. Ordenar vértices por grau decrescente
    vertices_ordenados = sorted(range(n), key=lambda v: len(grafo[v]), reverse=True)

    cores = [-1] * n  # -1 significa "não colorido"
    cor_atual = 0     # começamos com a cor 1

    # 2. Percorrer a lista de vértices ordenados
    for v in vertices_ordenados:
        if cores[v] == -1:      # se ainda não tem cor
            cor_atual += 1      # cria uma nova cor
            cores[v] = cor_atual

            # 3. Tentar colorir outros vértices compatíveis com mesma cor
            for u in vertices_ordenados:
                if cores[u] == -1:  # ainda sem cor
                    # checar se nenhum vizinho tem essa cor
                    if all(cores[viz] != cor_atual for viz in grafo[u]):
                        cores[u] = cor_atual

    return cores


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

cores = welsh_powell(grafo)

print("Coloração encontrada:", cores)
print("Número de cores usadas:", max(cores))