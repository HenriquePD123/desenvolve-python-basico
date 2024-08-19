import string

def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verifica se contém pelo menos uma letra maiúscula
    if not any(c.isupper() for c in senha):
        return False
    
    # Verifica se contém pelo menos uma letra minúscula
    if not any(c.islower() for c in senha):
        return False
    
    # Verifica se contém pelo menos um número
    if not any(c.isdigit() for c in senha):
        return False
    
    # Verifica se contém pelo menos um caractere especial
    caracteres_especiais = string.punctuation
    if not any(c in caracteres_especiais for c in senha):
        return False
    
    return True

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False