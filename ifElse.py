# > maior que / < menor que
# >= menor ou igual / < menor ou igual
# == igual
# != diferente


vendas = 6502
metas = 7550

if vendas > metas:
    print("Você atingiu a meta!")
else: 
    print(f"Ainda faltam vender {metas - vendas}")


vendas = 1500
meta1 = 1300 # ganha 10%
meta2 = 2000 # ganha 20%

if vendas >= meta2: 
    bonus = 0.2 * vendas
elif vendas >= meta1:
        bonus = 0.1 * vendas

print("Bonus de" , bonus)