'''
Estrutura de decisão no Python
Classificação
    > Simples
    > Composta
    > Encadeada
    > Aninhada
'''

print('Decisão simples - è dada por uma única decisão')

idade = 18

if idade >= 18:
    print(" Pode ser preso")

print(15*'-')    


print('Composta - Uma única decisão e uma respota padrão')

if idade >=18:
    print('Pode ser preso')


else: 
    print( 'Não posso ajudar')


print(15*'-')

print('Encadeada é dada por mais de uma decição e por uma respota padrão')

if idade >=18:
    print('Pode ser preso')

elif idade <=18:
    print('Menor de idade')

else: 
    print( 'Não posso ajudar')


print(15*'-')


print('Aninhada - Possui uma estrutura de decisão dentro da outra')

classificacao = 16
ingresso = False

if classificacao >=16:
    if ingresso == True:
        print('Pode assistir ao filme')
    else:
        print('Não pode assistir ao filme') 

else:
    print('Não pode assitir ao filme')   



