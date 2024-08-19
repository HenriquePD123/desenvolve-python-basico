def main():
    # Solicita ao usuário uma quantidade indefinida de números inteiros
    numeros = []
    
    print("Digite pelo menos 4 números inteiros. Para terminar a entrada, digite 'fim'.")
    
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            if len(numeros) < 4:
                print("Você deve inserir pelo menos 4 números. Tente novamente.")
            else:
                break
        else:
            try:
                numero = int(entrada)
                numeros.append(numero)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

    # A lista original
    print("Lista original:", numeros)
    
    # Os 3 primeiros elementos
    primeiros_3 = numeros[:3]
    print("Os 3 primeiros elementos:", primeiros_3)
    
    # Os 2 últimos elementos
    ultimos_2 = numeros[-2:]
    print("Os 2 últimos elementos:", ultimos_2)
    
    # A lista invertida (do fim para o começo)
    lista_invertida = numeros[::-1]
    print("Lista invertida:", lista_invertida)
    
    # Os elementos de índice par (0, 2, 4, ...)
    elementos_indice_par = numeros[::2]
    print("Elementos de índice par:", elementos_indice_par)
    
    # Os elementos de índice ímpar (1, 3, 5, ...)
    elementos_indice_impar = numeros[1::2]
    print("Elementos de índice ímpar:", elementos_indice_impar)

if __name__ == "__main__":
    main()