from itertools import combinations

lista = [1, 2, 3, 4]
subconjuntos = []

for x in range(0, len(lista) + 1):
    if x == 0:
        subconjuntos.append([])
    if x == 1:
        for item in lista:
            subconjuntos.append([item])
    if x > 1:
        tupla_combinacoes = list(map(list, list(combinations(lista, x))))
        subconjuntos.extend(tupla_combinacoes)

print(subconjuntos)