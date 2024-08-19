# Mapeamento de emojis
emojis = {
    ":smile:": "😊",
    ":heart:": "❤️",
    ":thumbs_up:": "👍",
    ":sunglasses:": "😎",
    ":cry:": "😢",
    ":laughing:": "😆",
    ":angry:": "😠",
    ":winking:": "😉",
    ":star:": "⭐",
    ":clap:": "👏"
}

# Função para exibir a lista de emojis e seus códigos
def exibir_emojis(emojis):
    print("Lista de emojis disponíveis:")
    for texto, emoji in emojis.items():
        print(f"{texto}: {emoji}")

# Função para codificar a frase usando emojis
def codificar_frase(frase, emojis):
    for texto, emoji in emojis.items():
        frase = frase.replace(texto, emoji)
    return frase

# Exibe a lista de emojis disponíveis
exibir_emojis(emojis)

# Solicita ao usuário uma frase codificada
frase_codificada = input("\nDigite a frase codificada usando os códigos dos emojis (por exemplo, ':smile: :heart:'): ")

# Decodifica a frase e exibe o resultado
frase_emojizada = codificar_frase(frase_codificada, emojis)
print(f"Frase emojizada: {frase_emojizada}")