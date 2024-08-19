# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Solicita se o usuário já jogou pelo menos 3 jogos de tabuleiro
jogou_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False) ").strip().capitalize()

# Converte a resposta para um valor booleano
jogou_3_jogos = jogou_3_jogos == 'True'

# Solicita o número de jogos vencidos
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica se o usuário atende aos critérios para ingressar no clube
apto_para_ingressar = (16 <= idade <= 18) and jogou_3_jogos and (vitorias >= 1)

# Imprime se o usuário está apto para ingressar no clube
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto_para_ingressar}")