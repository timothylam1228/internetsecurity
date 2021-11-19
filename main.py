# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg;
sg.theme('Dark Blue 3')   # Add a little color to your windows
fontSize = 20

des_layout = [[sg.Text('DES', font="Helvetica "  + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
        [sg.Text('Input the key size'), sg.Input()],
            [sg.OK(), sg.Cancel()]]

triple_des_layout = [[sg.Text('Triple DES', font="Helvetica "  + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
        [sg.Text('Input the key size'), sg.Input()],
            [sg.OK(), sg.Cancel()]]

aes_layout =  [[sg.Text('AES', font="Helvetica "  + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
        [sg.Text('Input the key size'), sg.Input()],
            [sg.OK(), sg.Cancel()]]

rsa_layout = [[sg.Text('RSA', font="Helvetica "  + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
        [sg.Text('Input the key size'), sg.Input()],
            [sg.OK(), sg.Cancel()]]

layout = [[sg.TabGroup([[sg.Tab('DES', des_layout), sg.Tab('Triple DES', triple_des_layout),sg.Tab('AES',aes_layout),sg.Tab('RSA',rsa_layout)]])]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event)
    if event == 'OK':
        print(values)
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
