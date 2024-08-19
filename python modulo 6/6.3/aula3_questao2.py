def extrair_dominios(urls):
    """Extrai o nome do domínio das URLs."""
    dominios = [url[4:-4] for url in urls]
    return dominios

def main():
    # Lista de URLs fornecidas
    urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
    
    # Extrai os domínios das URLs
    dominios = extrair_dominios(urls)
    
    # Imprime a lista de domínios
    print("URLs:", urls)
    print("Domínios:", dominios)

if __name__ == "__main__":
    main()