import os
# import datetime
# import pyautogui 

# pyautogui.press("win")
# pyautogui.write("note")

# print(os.listdir("arquivos"))
# print(datetime.date.today())

lista = os.listdir("arquivos")

for arquivo in lista:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}" , f"arquivos/22/{arquivo}")
        else: 
            os.rename(f"arquivos/{arquivo}" , f"arquivos/23/{arquivo}") 



