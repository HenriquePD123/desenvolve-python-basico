import re

def calcular_digito_verificador(digitos, multiplicadores):
    soma = sum(int(d) * m for d, m in zip(digitos, multiplicadores))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos e não é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return "Inválido"
    
    # Calcula o primeiro dígito verificador
    multiplicadores1 = list(range(10, 1, -1))
    digitos1 = cpf[:9]
    primeiro_digito = calcular_digito_verificador(digitos1, multiplicadores1)
    
    # Calcula o segundo dígito verificador
    multiplicadores2 = list(range(11, 1, -1))
    digitos2 = cpf[:9] + str(primeiro_digito)
    segundo_digito = calcular_digito_verificador(digitos2, multiplicadores2)
    
    # Verifica se os dígitos calculados correspondem aos dígitos fornecidos
    if cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
        return "Válido"
    else:
        return "Inválido"

# Programa principal
cpf_usuario = input("Digite o CPF (XXX.XXX.XXX-XX): ")
resultado = validar_cpf(cpf_usuario)
print(resultado)