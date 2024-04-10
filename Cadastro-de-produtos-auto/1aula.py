#Passo a passo do projeto 

import pyautogui
import time

# Passo 1 - Entrar no Sistema da empresa
    # # https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 0.3
pyautogui.press("win")
time.sleep(3)
pyautogui.write("Chrome")
time.sleep(3)
pyautogui.press("enter")

time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
    
# Passo 2 - Fazer Login
time.sleep(5)
pyautogui.click(x=460, y=362)
pyautogui.write("email@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)
time.sleep(3)
pyautogui.press("enter")
# Passo 4 - Cadastrar produtos
time.sleep(3)
for linha in tabela.index:
    pyautogui.click(x=634, y=250)
    # codigo do produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar produto
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 5 - Repetir isso ate acabar a base de dados

