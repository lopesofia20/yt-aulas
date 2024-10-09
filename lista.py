#listas
    #lista = [1, 29, 561, 652, 26, 786, 45721]
    #
    #tLista = sum(lista)
    #print(f"O total de vendar foi de: ",tLista)
    #
    ##tamanho da lista
    #tamanho = len(lista)
    #print(f"Você vendeu {tamanho} itens")
    #print(max(lista))
    #print(min(lista))


produtos = ["celular", "tablet", "smartwatch", "buds", "capinha"]

    #find = input("Pesquise pelo produto: ")
    #find = find.lower()
    #print(find in produtos)


#adicionar um item
produtos.append("notebook")
print(produtos)

#remover um item
produtos.remove("tablet") #remove por texto
print(produtos)

produtos.pop(0) #remove por posição
print(produtos)

#editar um item
lista = [29, 652, 26, 786]
lista[0] = 42

print(lista)

#contar quantas vezes um item aparece na lista

print(produtos.count("buds"))

#ordenar uma lista
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)