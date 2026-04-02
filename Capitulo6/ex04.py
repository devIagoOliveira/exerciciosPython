numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

quadrados = [x ** 2 for x in numeros]
quadradosPar = [x ** 2 for x in numeros if x % 2 == 0]

divisao = [x / 2 for x in numeros]

print(quadrados)
print(quadradosPar)
print(divisao[1])