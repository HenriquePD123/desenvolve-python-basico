# Solicita o número do celular ao usuário
numero = input("Digite o número: ")

# Remove qualquer caractere que não seja dígito (para garantir que estamos lidando apenas com números)
numero = ''.join(filter(str.isdigit, numero))

# Verifica o comprimento do número e o formata
if len(numero) == 8:
    # Se o número tem 8 dígitos, adiciona o 9 na frente
    numero_completo = '9' + numero
elif len(numero) == 9:
    # Se o número já tem 9 dígitos, verifica se o primeiro dígito é 9
    if numero[0] != '9':
        print("Número inválido: deve começar com 9")
        exit()
    numero_completo = numero
else:
    print("Número inválido: deve ter 8 ou 9 dígitos")
    exit()

# Adiciona o separador "-" e imprime o número formatado
numero_formatado = numero_completo[:5] + '-' + numero_completo[5:]
print(f"Número completo: {numero_formatado}")