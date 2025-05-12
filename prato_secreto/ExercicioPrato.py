import random

prato_secreto = ["l asanha", "hamburguer", "pizza", "sushi", "strogonoff"]
tentativas = 5

prato_secreto = random.choice(prato_secreto)
print(prato_secreto)


print("Tente adivinhar qual é o Prato Secreto da rodada!")

for tentativa in range(1,tentativas +1):
    print(f"Tentativa {tentativa} de {tentativas} Digite o prato:")
    palpite = input("informe sua tentativa:")

    if palpite == prato_secreto:
        print("Parabéns, Você acertou!!")
        break
    else:
        print("Tente Novamente!!")
    

