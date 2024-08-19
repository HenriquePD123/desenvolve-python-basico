def substituir_vogais(frase):
    # Definir as vogais
    vogais = "aeiouAEIOU"
    
    # Usar list comprehension para substituir as vogais por '*'
    frase_modificada = ''.join([char if char not in vogais else '*' for char in frase])
    
    return frase_modificada

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Substitui as vogais por '*'
frase_modificada = substituir_vogais(frase)

# Imprime a frase modificada
print("Frase modificada:", frase_modificada)