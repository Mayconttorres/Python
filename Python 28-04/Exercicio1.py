
numero_secreto = 5


print("Tente adivinhar o número secreto!")

tentativa = input("Qual o número secreto?")

Retorno_certo = "Boa, Você acertou"



if int(tentativa) == numero_secreto:
    print(Retorno_certo)

elif int(tentativa) > numero_secreto:
    print(" O número informado é maior do que o número secreto ")

elif int(tentativa) < numero_secreto:
    print(" O Valor informado é menor do que o Número secreto ")



 



# Inicializa a tentativa com um valor que não seja o número secreto

""" numero_secreto = 5
tentativa = 0

print('Tente adivinhar qual o número secreto!')


while int(tentativa) != numero_secreto:
    tentativa = input("Qual o número secreto? ")

    if int(tentativa) == numero_secreto:
        print("Boa, você acertou!")

    elif int(tentativa) > numero_secreto:
        print("O número informado é maior do que o número secreto.")

    elif int(tentativa) < numero_secreto:
        print("O valor informado é menor do que o número secreto.")


 """
