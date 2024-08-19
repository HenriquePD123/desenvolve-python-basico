def obter_nome_mes(numero_mes):
    # Lista com os nomes dos meses
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[numero_mes - 1]  # Ajusta o índice para a lista

# Solicita a data de nascimento ao usuário
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Divide a data em dia, mês e ano
dia, mes, ano = data.split('/')

# Converte o mês para um número inteiro
mes = int(mes)

# Obtém o nome do mês
nome_mes = obter_nome_mes(mes)

# Imprime a data formatada
print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")