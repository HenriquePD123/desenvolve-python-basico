import random

def gerar_lista(tamanho, intervalo):
    """Gera uma lista de tamanho especificado com números aleatórios dentro do intervalo dado."""
    return [random.randint(intervalo[0], intervalo[1]) for _ in range(tamanho)]

def encontrar_intervalo_max_negativos(lista):
    """Encontra o intervalo com a maior quantidade de números negativos na lista."""
    max_negativos = 0
    intervalo_max_neg = (0, 0)
    
    n = len(lista)
    for i in range(n):
        negativos = 0
        for j in range(i, n):
            if lista[j] < 0:
                negativos += 1
            if negativos > max_negativos:
                max_negativos = negativos
                intervalo_max_neg = (i, j)
    
    return intervalo_max_neg

def main():
    # Gera a lista com 20 elementos aleatórios entre -10 e 10
    lista = gerar_lista(20, (-10, 10))
    
    # Imprime a lista original
    print("Original:", lista)
    
    # Encontra o intervalo com a maior quantidade de números negativos
    intervalo_max_neg = encontrar_intervalo_max_negativos(lista)
    
    # Remove o intervalo da lista
    if intervalo_max_neg != (0, 0):
        del lista[intervalo_max_neg[0]:intervalo_max_neg[1] + 1]
    
    # Imprime a lista editada
    print("Editada:", lista)

if __name__ == "__main__":
    main()