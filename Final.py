import os
from tkinter.filedialog import askdirectory
import shutil

nome = askdirectory()
print(nome)

list = os.listdir(nome)
print(list)


#fazer backup
nome_pasta_backup = "backup"
completo_backup = f"{nome}/{nome_pasta_backup}"
if not os.path.exists(completo_backup):
    os.mkdir(nome_pasta_backup)


# for arquivo in list:
#     print(arquivo)
#     arq = f"{nome}/{arquivo}"
#     final = f"{completo_backup}/{arquivo}"