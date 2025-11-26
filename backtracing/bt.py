def pode_colorir(grafo, cor_atual, cores, v):
    for viz in grafo[v]:
        if cores[viz] == cor_atual:
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

            cores[v] = 0  # backtrack

    return False


def colorir_escalavel(grafo):
    n = len(grafo)
    cores = [0] * n

    # tenta com 1 cor, 2 cores, 3 cores... até n cores
    for max_cores in range(1, n + 1):
        print(f"Tentando com {max_cores} cores...")

        cores = [0] * n  # reseta
        if colorir_recursivo(grafo, max_cores, cores):
            print("Coloração encontrada!")
            return cores, max_cores

    return None, None


# -----------------------------
# EXEMPLO DE GRAFO
# -----------------------------
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
