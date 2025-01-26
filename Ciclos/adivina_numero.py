from random import randint, random

print('*** Adivina el número ***')

numero_secreto = randint(1, 100)
numero_jugador = 0
intentos = 0

while numero_jugador != numero_secreto:
    numero_jugador = int(input('Adivina un número entre 1 y 100: '))
    if numero_jugador > numero_secreto:
        print('Tu número es muy alto')
        intentos += 1
    elif numero_jugador < numero_secreto:
        print('Tu número es muy bajo')
        intentos += 1
    elif numero_jugador == numero_secreto:
        print(f'Felicidades, acertaste el número en {intentos} intentos')