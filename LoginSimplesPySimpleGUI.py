import PySimpleGUI as sg

layout=[
    [sg.Text("Usuário")],
    [sg.Input(key="usuario")],
    [sg.Text("Senha")],
    [sg.Input(key="senha")],
    [sg.Button("Login")],
    [sg.Text("",key="mensagem")],

]

window = sg.Window("Login",layout=layout)

while True:
    evento,valor = window.read()
    if evento == sg.WIN_CLOSED:
        break
