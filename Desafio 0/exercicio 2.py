lista = [3, 8, 50, 5, 1, 18, 12]
lista = sorted(lista, reverse=True)
lista_parciais = []
resultado_final = []
menor = 999_999_999_999

print('Lista de elementos: ', lista)
for x in range(len(lista)):
    for y in range(1, len(lista)):
        if x != y and lista[x] - lista[y] > 0:
            lista_parciais.append([lista[x], lista[y], lista[x] - lista[y]])
            if lista[x] - lista[y] < menor:
                menor = lista[x] - lista[y]

for itens in lista_parciais:
    if itens[2] == menor:
        resultado_final.append(tuple([itens[0], itens[1]]))
print("Números com a menor diferença absoluta: ", resultado_final)
