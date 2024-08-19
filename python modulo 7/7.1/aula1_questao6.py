def sao_anagramas(palavra1, palavra2):
    """
    Verifica se palavra1 é um anagrama de palavra2.
    """
    return sorted(palavra1) == sorted(palavra2)

# Solicita a frase e a palavra objetivo ao usuário
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

# Divide a frase em palavras
palavras = frase.split()

# Encontra os anagramas
anagramas = [palavra for palavra in palavras if sao_anagramas(palavra, palavra_objetivo)]

# Imprime os anagramas encontrados
print("Anagramas:", anagramas)