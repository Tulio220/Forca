"""
Projeto: Adivinhe o número

Descrição: Neste jogo, o programa escolhe aleatoriamente um número entre 1 e 100. O jogador deve tentar adivinhar o número correto dentro de um número limitado de tentativas.

Regras:

O programa escolhe um número aleatório entre 1 e 100.
O jogador tem no máximo 10 tentativas.
O jogador faz uma suposição fornecendo um número.
O programa informa ao jogador se o número correto é maior ou menor do que a suposição feita.
O jogador continua fazendo suposições até adivinhar corretamente o número ou esgotar o número de tentativas.
Funcionalidades adicionais:

No início do jogo, o programa exibe uma mensagem de boas-vindas e explica as regras do jogo.
O programa mantém um registro do número de tentativas do jogador.
Ao final do jogo, o programa informa se o jogador adivinhou corretamente o número ou não, e exibe o número de tentativas realizadas.
O programa pergunta se o jogador deseja jogar novamente.
Dicas:

Você pode usar a biblioteca random em Python para gerar o número aleatório.
Utilize estruturas de controle como loops e condicionais para implementar a lógica do jogo.
Lembre-se de validar a entrada do jogador, garantindo que seja um número dentro do intervalo correto.
"""

import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    numero_tentativas = 10
    tentativas_feitas = 0

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while tentativas_feitas < numero_tentativas:
        tentativa = int(input("Digite a sua suposição: "))

        if tentativa < 1 or tentativa > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue

        tentativas_feitas += 1

        if tentativa < numero_secreto:
            print("O número correto é maior do que a sua suposição.")
        elif tentativa > numero_secreto:
            print("O número correto é menor do que a sua suposição.")
        else:
            print("Parabéns! Você acertou o número!")
            print("Número de tentativas: ", tentativas_feitas)
            break

    if tentativas_feitas == numero_tentativas:
        print("Você esgotou o número de tentativas.")
        print("O número correto era:", numero_secreto)

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        adivinhe_o_numero()

adivinhe_o_numero()
