import random
print("+-------------------------+")
print("|---- JOGO DO ADVINHA ----|")
print("+-------------------------+")
print("* regras: Você tem 5 chances de acertar um número de 1 a 20")

choice_pc = random.randint(1, 20)
cont = 0

#print(choise_pc)

while cont < 5:
    
    choice_user = int(input("Escolha um número de 1 a 20: "))
    
    if choice_user == choice_pc:
        print("-------------------------")
        print("Você acertou! Parabéns!!!")
        print("-------------------------")
        break
    elif cont == 4:
        print("Game Over!!!")
        break
    elif choice_user > choice_pc:
        print("Muito Alto.")
        cont += 1
    elif choice_user < choice_pc:
        print("Muito Baixo.")
        cont += 1
    
        

print(f"O número certo era {choice_pc}")
        
