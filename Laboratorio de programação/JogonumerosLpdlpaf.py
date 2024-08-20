import random

numero_secreto = random.randint(1, 100)
acertou = False
print(f"Bem vindo ao Jogo de advinhação, Você consegue acertar o numero ?")
nome_usuario = input("qual o seu nome?: ")
tentarnovamente = 1
while tentarnovamente == 1 :
    nivel = input('''Qual o nivel do jogo? 
    1 - Fácil
    2 - Médio
    3 - Dificil ''')
    nivel_do_jogo = int(nivel)

    if(nivel_do_jogo == 1):
        tentativas = 10
    if(nivel_do_jogo == 2):
        tentativas = 5
    if(nivel_do_jogo == 3):
        tentativas = 3

    
    numpalpites = 0

    for i in range(1, tentativas+1):
        palpite_usuario = input("qual o seu palpite? ")
        palpite = int(palpite_usuario)
        print(f"{nome_usuario} deu o palpite {palpite}")
     

        if (palpite == numero_secreto):
            print(f"{nome_usuario} você acertou o numero {numero_secreto}")
            acertou = True
            numpalpites += 1
            break

        else :
            numpalpites += 1
            if(palpite < numero_secreto):
                print(f"{nome_usuario} você errou para baixo ! O numero secreto é maior")
            else:
                print(f"{nome_usuario} você errou para cima ! O numero secreto é menor")
    if (acertou == True):
        print(f"Parabens {nome_usuario} você ganhou o jogo com {numpalpites} palpites")
    else:
        print(f"Game Over, Tente Novamente")

    tentarnovamente = int(input("Deseja tentar novamente?, 1- Sim 2- Não "))



print(f"Jogo Encerrado, Obrigado!")
