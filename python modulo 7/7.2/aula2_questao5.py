import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 2:
            return palavra
        primeira_letra = palavra[0]
        ultima_letra = palavra[-1]
        letras_internas = list(palavra[1:-1])
        random.shuffle(letras_internas)
        return primeira_letra + ''.join(letras_internas) + ultima_letra

    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(p) for p in palavras]
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)