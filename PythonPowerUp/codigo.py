import pyautogui
import time
import pandas

tabela = pandas.read_csv('PythonPowerUp/produtos.csv')

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(15)

pyautogui.click(x=551, y=414)
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab')
pyautogui.write('sua senha')
pyautogui.click(x=663, y=559)

time.sleep(15)

for linha in tabela.index:
    pyautogui.click(x=441, y=291)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)

