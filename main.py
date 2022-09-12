import PySimpleGUI as sg
def paro_ou_impar(número):
    if número % 2 == 0:
        v = f"O número {número} é par!"
        return v
    else:
        v = f"O número {número} é ímpar!"
        return v
# Theme
sg.theme('Dark Grey 13')
# Layout
layout = [
    [sg.Text("Par ou Ímpar")],
    [sg.InputText(key="Valor")],
    [sg.Button("Conferir"), sg.Button("Cancelar")],
    [sg.Text("", key="parimpar")],
]
window = sg.Window("Par ou Ímpar", layout)

while True:
    evento, valores = window.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == "Cancelar":
        sg.popup('Clique na tecla abaixo para fechar')
        break
    if evento == "Conferir":

        número = int(valores["Valor"])
        window["parimpar"].update(paro_ou_impar(número))

window.close()
