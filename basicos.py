salario = 1900
vr = 350
lucro = salario - vr
porcentagem = lucro * 0.1
print("O lucro foi de: ",round(porcentagem, 1)) # o comando Round arredonda o resultado da conta
tempo = 2553;
anos = 2553 / 12;
meses = 2553 % 12;
print(f"O tempo deu {tempo} dias, {anos} anos e {meses} meses" )

email = "VcEmail@gmail.com"
email = email.upper()#deixa texto maisucula
print(email) 

email = email.lower() #deixa texto minuscula
print(email)
print(email.find("@")) #encontra o caracter indicado na posicao e retorna -1 quando nao encontrar
print(len(email)) #retoprna o tamanho do texto
print(email[0]) #pegar um caractere
print(email[:7]) #pegar ate o indice indicado
Nemail = email.replace("gmail.com", "capivara.com")  #trocar um pedaço do texto por outro
print(Nemail) #imprimir o texto alterado

nome = "vitoria lopes"
print(nome.capitalize()) #deixa  a primeira letra maiuscula
print(nome.title()) #deixa a primeira letra de cada palavra maiuscula



