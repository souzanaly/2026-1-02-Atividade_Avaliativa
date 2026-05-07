numero = int(input("Digite um número: "))
soma_divisores = 0

# Procuramos divisores de 1 até a metade do número
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

if soma_divisores == numero:
    print(f"{numero} é perfeito")
else:
    print(f"{numero} não é perfeito")