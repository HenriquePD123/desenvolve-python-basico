import random

def encrypt(nomes):
    # Gera uma chave aleatória entre 1 e 10
    chave_aleatoria = random.randint(1, 10)
    
    # Função auxiliar para criptografar um único caractere
    def criptografar_caractere(c, chave):
        novo_codigo = ord(c) + chave
        # Garante que o caractere resultante esteja dentro do intervalo visível
        if novo_codigo > 126:
            novo_codigo = 33 + (novo_codigo - 127)  # Volta para o intervalo visível
        return chr(novo_codigo)
    
    # Criptografa cada nome na lista usando a chave aleatória
    nomes_criptografados = [''.join(criptografar_caractere(c, chave_aleatoria) for c in nome) for nome in nomes]
    
    return nomes_criptografados, chave_aleatoria

# Exemplo de uso
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print("Chave de criptografia:", chave)
print("Nomes criptografados:", nomes_criptografados)