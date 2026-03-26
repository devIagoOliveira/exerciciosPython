print("-" * 55)
print("----------------- JOKENPÔ (2 Players) -----------------")
print("-" * 55)
print("Bem vindos! Cada jogador escolhe uma das opções válidas")

valid_options = ("pedra", "papel", "tesoura")
print("Opções válidas", valid_options)
print("-" * 55)

while True:

    jogador1 = input("Jogador 1, digite sua jogada: ").strip().lower()
    jogador2 = input("Jogador 2, digite sua jogada: ").strip().lower()

    print("-" * 55)
    print("Jogador 1 escolheu:", jogador1)
    print("Jogador 2 escolheu:", jogador2)
    print("-" * 55)

    if jogador1 not in valid_options or jogador2 not in valid_options:
        print("Uma ou mais jogadas estão inválidas, insira novamente")

    elif jogador1 == jogador2:
        print("Empatou!!!")
        print("\n       Fim de Jogo ...")
        break

    elif jogador1 == "pedra" and jogador2 == "papel" or \
    jogador1 == "papel" and jogador2 == "tesoura" or \
    jogador1 == "tesoura" and jogador2 == "pedra":
        print("Jogador 2 Ganhou! Parabéns!!!")
        print("\n       Fim de Jogo ...")
        break

    else:
        print("Jogador 1 Ganhou! Parabéns!!!")
        print("\n       Fim de Jogo ...")
        break





