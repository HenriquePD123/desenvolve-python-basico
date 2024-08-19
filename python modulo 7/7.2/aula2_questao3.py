import string

def normalizar_frase(frase):
    # Remove pontuações e espaços, e transforma a frase em minúsculas
    frase_normalizada = ''.join(char.lower() for char in frase if char.isalnum())
    return frase_normalizada

def eh_palindromo(frase):
    frase_normalizada = normalizar_frase(frase)
    return frase_normalizada == frase_normalizada[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if frase.lower() == 'fim':
        break

    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')