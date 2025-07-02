import string

def verificar_palindromo():
    texto = input("Digite uma palavra ou frase: ")

    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    if texto_limpo == texto_limpo[::-1]:
        print("Sim")
    else:
        print("Não")

verificar_palindromo()
