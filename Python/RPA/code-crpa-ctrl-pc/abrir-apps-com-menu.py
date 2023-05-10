import pyautogui

opcao = pyautogui.confirm('', buttons=['Excel', 'Notepad', 'Word'])

if opcao == 'Excel':
    print('Excel')
elif opcao == 'Notepad':
    print('Notepad')
elif opcao == 'Word':
    print('Word')
else:
    print('Erro no valor inserido.')