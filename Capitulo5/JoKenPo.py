print("-" * 50)
print("------------- Jo Ken Pô (2 Players) --------------")
print("-" * 50)
print("Welcome! Each player must choose one of the options")

valid_options = ("pedra", "papel", "tesoura")
print("Opções validas", valid_options)
print("-" * 25)

while True:

    jogador1 = input("Jogador 1, digite sua jogada: ").strip().lower()
    jogador2 = input("Jogador 2, digite sua jogada: ").strip().lower()

    print("-" * 25)
    print("Jogador 1 escolheu:", jogador1)
    print("Jogador 2 escolheu:", jogador2)
    print("-" * 25)

    if jogador1 not in valid_options or jogador2 not in valid_options:
        print("Uma ou mais jogadas estão inválidas, insira novamente")

    elif jogador1 == jogador2:
        print("Empatou!!!")

    elif jogador1 == "pedra" and jogador2 == "papel" or \
    jogador1 == "papel" and jogador2 == "tesoura" or \
    jogador1 == "tesoura" and jogador2 == "pedra":
        print("Jogador 2 Ganhou! Parabéns!!!")
        print("---- Fim de Jogo ... ----")
        break

    else:
        print("Jogador 1 Ganhou! Parabéns!!!")
        print("---- Fim de Jogo ... ----")
        break





