lista = [3, 8, 50, 5, 1, 18, 12]
lista = sorted(lista, reverse=True)
lista_resultados = []
resultado_final = []
menor = 999_999_999_999

print(lista)
for x in range(len(lista)):
    for y in range(1, len(lista)):
        if x != y and lista[x] - lista[y] > 0:
            lista_resultados.append([lista[x], lista[y], lista[x] - lista[y]])
            if lista[x] - lista[y] < menor:
                menor = lista[x] - lista[y]

for x in lista_resultados:
    if x[2] == menor:
        resultado_final.append(tuple([x[0], x[1]]))
print(resultado_final)
