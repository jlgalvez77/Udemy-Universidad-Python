print('*** Sistema de Calificación ***')
nota = float(input('Introduce la calificación (1-10): '))

if nota >= 9 and nota <= 10:
    print('La nota es A')
elif nota >= 8 and nota < 9:
    print('La nota es B')
elif nota >= 7 and nota < 8:
    print('La nota es C')
elif nota >= 6 and nota < 7:
    print('La nota es D')
elif nota >= 0 and nota < 6:
    print('La nota es F')
else:
    print('Valor Desconocido')