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
import random

dias_semana = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']
temp = []

for dia in dias_semana:
    for _ in range(0, 1):
        temperatura = random.randint(0, 80)
        asteriscos = '*' * temperatura
        print(f'{dia}: {asteriscos}')
        temp.append(temperatura)
    print()

temperaturas_string = ', '.join(map(str, temp))
print(f'As temperaturas foram {temperaturas_string}°C, respectivamente.')

