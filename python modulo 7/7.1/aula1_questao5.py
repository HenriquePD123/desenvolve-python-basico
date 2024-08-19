# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Conjunto de vogais
vogais = "aeiouAEIOU"

# Lista para armazenar os índices das vogais
indices_vogais = []

# Itera sobre a frase para verificar cada caractere
for i, char in enumerate(frase):
    if char in vogais:
        indices_vogais.append(i)

# Conta o número total de vogais
numero_vogais = len(indices_vogais)

# Imprime o número de vogais e os índices
print(f"{numero_vogais} vogais")
print(f"Índices {indices_vogais}")