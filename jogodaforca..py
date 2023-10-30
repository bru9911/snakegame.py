import random

def escolher_palavra():
    palavras = ["python", "java", "ruby", "javascript", "html", "css", "php", "swift"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_certas):
    resultado = ""
    for letra in palavra:
        if letra in letras_certas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_certas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(mostrar_palavra(palavra_secreta, letras_certas))

    while tentativas > 0:
        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_certas:
            print("Você já tentou essa letra. Tente novamente!")

        elif palpite in palavra_secreta:
            letras_certas.append(palpite)
            print("Letra correta!")

        else:
            tentativas -= 1
            print("Letra incorreta! Você tem {} tentativas restantes.".format(tentativas))

        print(mostrar_palavra(palavra_secreta, letras_certas))

        if set(letras_certas) == set(palavra_secreta):
            print("Parabéns! Você venceu!")
            break

    if tentativas == 0:
        print("Você perdeu! A palavra correta era '{}'.".format(palavra_secreta))

if __name__ == "__main__":
    jogo_da_forca()
