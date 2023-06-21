"""
Codifique um algoritmo que exiba um histograma da variação da temperatura durante a semana. Por exemplo, se as temperaturas forem: 19,21,,25,22,20,17 e 15°C, de domingo a sábado, respectivamente, o algortmo deverá exibir:
D: *************
S: *************
T:*******************
Q:******************
Q:*****************
S:*****************
S:***************
Suponha que as temperaturas sejam todas positivas e que nenhuma seja maior que 80°C.
"""
temperaturas = [19, 21, 25, 22, 20, 17, 15]

# Percorre cada temperatura na lista e exibe o histograma
for temperatura in temperaturas:
    # Cria uma string com '*' repetidos para representar a temperatura no histograma
    histograma = '*' * temperatura

    # Obtém o dia da semana correspondente ao índice da temperatura na lista
    dia_semana = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'][temperaturas.index(temperatura)]

    # Exibe o dia da semana e o histograma
    print(f"{dia_semana}: {histograma}")
