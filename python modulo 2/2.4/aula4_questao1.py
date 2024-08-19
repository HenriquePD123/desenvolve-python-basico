comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))
preco_m2 = float(input("valor do m2: "))
area = comprimento * largura
preco_total = area * preco_m2
print(f"O terreno possui {area}m2 e custa {preco_total:,.2f} ")