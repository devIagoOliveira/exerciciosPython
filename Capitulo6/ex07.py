def paresImpares(lista):
    par = 0
    impar = 0
    for x in lista:
        if x % 2 == 0:
            par += 1
        else:
            impar += 1
    
    dicNumbers = {'par' : par, 'impar': impar}
    return dicNumbers

# import ex07

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# n = ex07.paresImpares(lista)

# print(n)