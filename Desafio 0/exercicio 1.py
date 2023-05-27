n = int(input("Digite o número: "))
i = "*"
lista = []

for x in range(1, n+1):
    lista.append(f"{i * x}")

print(lista)