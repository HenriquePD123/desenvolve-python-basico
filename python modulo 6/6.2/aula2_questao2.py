import random

def main():
    # Gera aleatoriamente um valor entre 5 e 20 para num_elementos
    num_elementos = random.randint(5, 20)
    
    # Gera uma lista de valores aleatórios entre 1 e 10 com comprimento num_elementos
    elementos = [random.randint(1, 10) for _ in range(num_elementos)]
    
    # Calcula a soma e a média dos valores da lista
    soma_valores = sum(elementos)
    media_valores = soma_valores / num_elementos
    
    # Imprime a lista, a soma e a média dos valores
    print("Lista de elementos:", elementos)
    print("Soma dos valores:", soma_valores)
    print("Média dos valores:", round(media_valores, 2))

if __name__ == "__main__":
    main()