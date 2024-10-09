#brands = ["dior", "prada", "gucci", "versace", "louis vuitton"]
#preços = [16000, 23000, 19000, 62000, 35000]


brands = {"dior": 16000, "prada": 23000, "gucci": 19000, "versace": 62000, "louis vuitton": 35000}

#pegar um elemento do dicionario
print(brands["dior"])

#pegar quantidade de itens do dicionario
print(len(brands))

#retirar
brands.pop("prada")
print(brands)

#adicionar
brands["chanel"] = 45000
print(brands)

#existe item
if "prada" in brands:
    print("existe")
else: 
    print("este produto não existe")

#existe chave
if 60000 in brands.values():
    print("existe")
else: 
    print("este produto não existe")

#existe valor
if "versace" in brands.keys():
    print("existe")
else: 
    print("este produto não existe")


