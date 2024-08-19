def ler_lista(nome_lista):
    """Função para ler uma lista de números do usuário."""
    quantidade = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    print(f"Digite os {quantidade} elementos da {nome_lista}:")
    for _ in range(quantidade):
        valor = int(input())
        lista.append(valor)
    return lista

def combinar_listas(lista1, lista2):
    """Função para combinar duas listas de forma alternada."""
    lista_intercalada = []
    tamanho_minimo = min(len(lista1), len(lista2))
    
    # Intercala os elementos das duas listas
    for i in range(tamanho_minimo):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    
    # Adiciona os elementos restantes da lista maior
    if len(lista1) > len(lista2):
        lista_intercalada.extend(lista1[tamanho_minimo:])
    else:
        lista_intercalada.extend(lista2[tamanho_minimo:])
    
    return lista_intercalada

def main():
    # Lê as duas listas do usuário
    lista1 = ler_lista("lista 1")
    lista2 = ler_lista("lista 2")
    
    # Combina as listas
    lista_intercalada = combinar_listas(lista1, lista2)
    
    # Imprime a lista intercalada
    print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))

if __name__ == "__main__":
    main()