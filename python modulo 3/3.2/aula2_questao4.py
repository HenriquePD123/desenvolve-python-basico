# Solicita a classe do personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()

# Solicita os pontos de força e magia
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Inicializa a variável que irá armazenar a validade dos atributos
atributos_validos = False

# Valida os atributos com base na classe escolhida
if classe == 'guerreiro':
    atributos_validos = (forca >= 15 and magia <= 10)
elif classe == 'mago':
    atributos_validos = (forca <= 10 and magia >= 15)
elif classe == 'arqueiro':
    atributos_validos = (5 < forca <= 15 and 5 < magia <= 15)
else:
    print("Classe inválida.")

# Imprime se os pontos de atributo são consistentes com a classe escolhida
print(f"Pontos de atributo consistentes com a classe escolhida: {atributos_validos}")