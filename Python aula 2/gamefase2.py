import random

print(25*"#")
print("Descubra o numero secreto")
print(25*"#")
print("")
print(43*"#")
print("Você é capaz de descobrir o numero secreto?")
print(43*"#")


#Random escolhe valores de forma aleatoria


secreto_num = random.randrange(10,100) 
pontuacao = 100 
tentativas = 0
dificuldade = input("Escolha o nivel de dificuldade (facil, medio, dificil):").lower()
perda_pontos = 0



if dificuldade == "facil":
    tentativas = 30
    perda_pontos = 10
    
    
elif dificuldade == "medio":
    tentativas = 15
    perda_pontos = 20
    
elif dificuldade == "dificil":
    tentativas = 5
    perda_pontos = 50

chance = 1
while chance < tentativas:

#for chance in range(1,tentativas+1):
    print(f"Tentativa {chance} de {tentativas}")
    palpite = int(input("Informe seu palpite: "))

    if palpite < 10 or palpite > 100:
        print("Valor Invalido, favor informe um valor entre 10 e 100")
        continue

    print("Seu palpite é: {}".format(palpite))

    if (secreto_num == palpite):
        print("Você acertou miseravi")
        break   

    elif pontuacao == 0:
        print("Fim de jogo")
        break

    else:
        print("Você errou miseravi")
        pontuacao -= perda_pontos
        print(f"voce perdeu {perda_pontos}, restam ainda {pontuacao}")

    chance += 1














    





    
""" erro_perda = calcular_perda(dificuldade)
print(erro_perda)

tentativas = int(input("Quantas vezes deseja jogar? "))

palpite = input("Informe seu palpite: ")
for tentativa in range(1,tentativas+1):
    print(f"Tentativa {tentativa} de {tentativas}")
    palpite = input("Informe seu palpite: ")
    print("Seu palpite é: {}".format(palpite))
    if (secreto_num == int(palpite)):
        print("Você acertou miseravi")
        break
    else:
        print("Você errou miseravi")


print("Fim de jogo")  """



    
 
















""" tentativas = int(input("Quantas vezes deseja jogar? "))

for tentativa in range(1,tentativas+1):
    print(f"Tentativa {tentativa} de {tentativas}")
    palpite = input("Informe seu palpite: ")
    print("Seu palpite é: {}".format(palpite))
    if (secreto_num == int(palpite)):
        print("Você acertou miseravi")
        break
    else:
        print("Você errou miseravi")


print("Fim de jogo") """