lista = [2019, 450, 859, 2652]

meta = 800
p_bonus = 0.1

for venda in lista:
    if venda >= meta:
        bonus = p_bonus * venda
    else: 
        bonus = 0

    print(bonus)