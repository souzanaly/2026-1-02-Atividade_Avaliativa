# Lendo a quantidade de números
repeticoes = int(input("Digite a quantidade de números: "))

# Inicializando variáveis de controle
soma_total = 0
maior_valor = None
menor_valor = None
lista_numeros = []

# Laço para leitura e processamento inicial
for i in range(1, repeticoes + 1):
    valor = int(input(f"Informe o valor {i}: "))
    lista_numeros.append(valor)
    
    # Acumulando a soma
    soma_total += valor
    
    # Verificando o maior e o menor manualmente
    if maior_valor is None or valor > maior_valor:
        maior_valor = valor
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor

# Cálculo da média
media = soma_total / repeticoes

# Contagem de valores acima da média
quantidade_acima_media = 0
for n in lista_numeros:
    if n > media:
        quantidade_acima_media += 1

# Exibição dos resultados formatados
print(f"a soma total é {soma_total}")
print(f"a média é {media}")
print(f"o maior valor é {maior_valor}")
print(f"o menor valor é {menor_valor}")
print(f"a quantidade de valores acima da média é {quantidade_acima_media}")