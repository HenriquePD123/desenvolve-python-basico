import random

def main():
    # Gera 20 valores inteiros aleatórios entre -100 e 100 e os armazena em uma lista
    lista_original = [random.randint(-100, 100) for _ in range(20)]
    
    # Cria uma cópia da lista para ordená-la sem modificar a lista original
    lista_ordenada = sorted(lista_original)
    
    # Encontra os índices do maior e do menor valor da lista original
    maior_valor = max(lista_original)
    menor_valor = min(lista_original)
    indice_maior = lista_original.index(maior_valor)
    indice_menor = lista_original.index(menor_valor)
    
    # Imprime a lista ordenada
    print("Lista ordenada:", lista_ordenada)
    
    # Imprime a lista original
    print("Lista original:", lista_original)
    
    # Imprime o índice do maior valor
    print("Índice do maior valor:", indice_maior)
    
    # Imprime o índice do menor valor
    print("Índice do menor valor:", indice_menor)

if __name__ == "__main__":
    main()