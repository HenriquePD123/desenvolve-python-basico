#leitura de dados
fahrenheit = int(input("Digite a temperatura em fahreinheit: "))
#processamento
celsius = (fahrenheit - 32) * 5 / 9
#impressão de dados
print(f"{fahrenheit} graus Fahreinheit são equivalentes a {int(celsius)} graus Celsius")