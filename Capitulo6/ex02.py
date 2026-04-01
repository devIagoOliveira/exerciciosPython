def tabuada():
    num = int(input("Insira um número para ver a tabuada: "))
    for x in range(1, 11):
        print(f"{num} x {x} = {num * x}")
