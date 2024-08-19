distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

# Calcula o valor do frete com base na distância
if distancia <= 100:
    valor_frete = peso * 1.00
elif 101 <= distancia <= 300:
    valor_frete = peso * 1.50
else:
    valor_frete = peso * 2.00

# Adiciona uma taxa de R$10 para pacotes com peso superior a 10 kg
if peso > 10:
    valor_frete += 10

# Imprime o valor total do frete
print(f"Valor do frete: R${valor_frete:.2f}")