# Função para formatar o preço com separador de milhar e duas casas decimais
def formatar_preco(preco):
    return f"R${preco:,.2f}"

# Solicita os dados dos 3 produtos
produto1_nome = input("Digite o nome do produto 1: ")
produto1_preco = float(input("Digite o preço unitário do produto 1: "))
produto1_quantidade = int(input("Digite a quantidade do produto 1: "))

produto2_nome = input("Digite o nome do produto 2: ")
produto2_preco = float(input("Digite o preço unitário do produto 2: "))
produto2_quantidade = int(input("Digite a quantidade do produto 2: "))

produto3_nome = input("Digite o nome do produto 3: ")
produto3_preco = float(input("Digite o preço unitário do produto 3: "))
produto3_quantidade = int(input("Digite a quantidade do produto 3: "))

# Calcula o preço total da compra
total = (produto1_preco * produto1_quantidade +
         produto2_preco * produto2_quantidade +
         produto3_preco * produto3_quantidade)

# Imprime o total formatado
print(f"Total: {formatar_preco(total)}")