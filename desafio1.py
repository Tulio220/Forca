import random

# Lista de palavras secretas pré-definidas
palavras = ['python', 'programacao', 'computador', 'jogo', 'desenvolvimento']

def escolher_palavra():
    return random.choice(palavras)

def exibir_forca(vidas):
    forca = [
        '''
           +---+
               |
               |
               |
              ===''',
        '''
           +---+
           O   |
               |
               |
              ===''',
        '''
           +---+
           O   |
           |   |
               |
              ===''',
        '''
           +---+
           O   |
          /|   |
               |
              ===''',
        '''
           +---+
           O   |
          /|\\  |
               |
              ===''',
        '''
           +---+
           O   |
          /|\\  |
          /    |
              ===''',
        '''
           +---+
           O   |
          /|\\  |
          / \\  |
              ==='''
    ]
    print(forca[vidas])

def exibir_palavra(palavra_secreta, letras_corretas):
    for letra in palavra_secreta:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def jogar_novamente():
    resposta = input('Deseja jogar novamente? (s/n): ')
    return resposta.lower() == 's'

def jogo_da_forca():
    vidas_maximas = 6
    letras_corretas = []
    letras_erradas = []
    palavra_secreta = escolher_palavra()
    vidas = vidas_maximas

    print('Bem-vindo ao jogo da forca!')
    exibir_palavra(palavra_secreta, letras_corretas)

    while vidas > 0:
        letra = input('Digite uma letra: ')

        if letra in letras_corretas or letra in letras_erradas:
            print('Você já tentou essa letra. Tente novamente!')
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
            exibir_palavra(palavra_secreta, letras_corretas)

            if set(letras_corretas) == set(palavra_secreta):
                print('Parabéns! Você venceu!')
                break

        else:
            letras_erradas.append(letra)
            exibir_forca(vidas)
            print('Letras erradas:', letras_erradas)
            vidas -= 1

    if vidas == 0:
        print('Você perdeu! A palavra secreta era:', palavra_secreta)

    if jogar_novamente():
        jogo_da_forca()

jogo_da_forca()
