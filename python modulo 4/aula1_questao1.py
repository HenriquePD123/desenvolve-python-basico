def verificar_valor():
    # Leitura do valor
    x = float(input("Digite um valor: "))
    
    # Verifica se o valor é maior que 5
    if x > 5:
        print("Maior que 5")
    
    # Imprime "fim" independentemente da condição
    print("Fim")

# Chamada da função
verificar_valor()