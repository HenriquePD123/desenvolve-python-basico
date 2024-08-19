import random
from collections import Counter

def main():
    # Gera duas listas com 20 valores inteiros aleatórios entre 0 e 50
    lista1 = [random.randint(0, 50) for _ in range(20)]
    lista2 = [random.randint(0, 50) for _ in range(20)]
    
    # Cria uma lista de interseção contendo valores únicos que aparecem em ambas as listas
    interseccao = list(set(lista1) & set(lista2))
    
    # Ordena a lista de interseção
    interseccao.sort()
    
    # Conta a quantidade de vezes que cada elemento aparece em cada lista
    contagem_lista1 = Counter(lista1)
    contagem_lista2 = Counter(lista2)
    
    # Imprime as duas listas
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    
    # Imprime a lista de interseção ordenada
    print("Interseccao -", interseccao)
    
    # Imprime a contagem de cada elemento em ambas as listas
    print("Contagem:")
    for valor in interseccao:
        print(f"{valor}: (lista1={contagem_lista1[valor]}, lista2={contagem_lista2[valor]})")

if __name__ == "__main__":
    main()