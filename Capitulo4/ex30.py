altura = float(input("Qual a sua altura? "))
peso = float(input("Qual seu peso? "))

IMC = peso / (altura * altura)

print(f"Seu índice de massa corporal (IMC) é: {IMC:.2f}")

if IMC < 18.5:
    print("Abaixo do peso"),
elif IMC < 24.9:
    print("Peso Ideal/Normal"),
elif IMC < 29.9:
    print("Sobrepeso"),
elif IMC < 34.9:
    print("Obesidade Grau 1"),
elif IMC < 39.9:
    print("Obesidade Grau 2"),
else:
    print("Obesidade Grau 3 (Mórbida)")
