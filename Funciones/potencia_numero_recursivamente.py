# Potencia de un número de forma recursiva

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    

print(potencia(4, 5))