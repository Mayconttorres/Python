lista = [5, 2, 5, 8, 1, 8, 3] # lista original com itens duplicados
lista_nova = [] # lista nova onde vamos anexar os numeros sem duplicidade

for i in lista: #for para ler o array
    if i not in lista_nova: # not in para ler e verificar duplicado
        lista_nova.append(i) # append - depois de ler ele adiciona o item na lista vazia

    print(lista_nova)