import csv
from collections import defaultdict

def processar_arquivo_spotify(caminho_arquivo):
    # Dicionário para armazenar a música mais tocada de cada ano
    mais_tocada_por_ano = defaultdict(lambda: ["", 0])  # Valor padrão: [nome_música, streams]

    # Abrir e ler o arquivo CSV
    with open(caminho_arquivo, mode='r', encoding='latin-1') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        
        # Ignorar o cabeçalho
        next(leitor_csv)

        for linha in leitor_csv:
            if len(linha) < 10:
                continue  # Pular linhas inválidas

            track_name = linha[0].strip('"')
            artist_name = linha[1].strip('"')
            artist_count = int(linha[2])
            released_year = int(linha[3])
            streams = int(linha[8])

            # Verificar se a linha está dentro do intervalo de anos de 2012 a 2022
            if 2012 <= released_year <= 2022:
                # Atualizar a música mais tocada para o ano específico
                if streams > mais_tocada_por_ano[released_year][1]:
                    mais_tocada_por_ano[released_year] = [track_name, artist_name, streams]

    # Criar a lista final com as músicas mais tocadas de cada ano
    lista_final = [
        [info[0], info[1], ano, info[2]]
        for ano, info in mais_tocada_por_ano.items()
        if 2012 <= ano <= 2022
    ]
    
    # Ordenar a lista final pelos anos
    lista_final.sort(key=lambda x: x[2])

    return lista_final

# Caminho do arquivo CSV
caminho_arquivo = 'spotify-2023.csv'
resultado = processar_arquivo_spotify(caminho_arquivo)
print(resultado)