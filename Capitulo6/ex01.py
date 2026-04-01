def triangulo(n1, n2, n3):
    if n1 == n2 and n1 == n3:
        print("Equilátero")
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print("Isósceles")
    else:
        print("Escaleno")
