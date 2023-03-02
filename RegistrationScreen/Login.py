import PySimpleGUI as sg

# Layout


sg.theme('Reddit')
layout = [
    [sg.Text('login')],
    [sg.Input(key='login')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Cadastrar')]
]
# Janela
janela = sg.Window('Acesso', layout)

# Ler os eventos
while True:
    event, values = janela.Read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'dados':
        login = values['login']
        senha = values['senha']
