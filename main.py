# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
from base64 import b64encode

import codecs
sg.theme('Dark Blue 3')   # Add a little color to your windows
fontSize = 25

des_layout = [[sg.Text('DES', font="Helvetica"+str(fontSize)) ,sg.Combo(['ECE','CBC','CFB','OFB','CTR'])],
              [sg.Text('Key size is fixed at 56 bytes')],
              [sg.Text('Input the message to encrypt'), sg.Input()]
              ]

triple_des_layout = [[sg.Text('Triple DES', font="Helvetica " + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
                     [sg.Text('Input the key size'+str(fontSize)), sg.Input()]]

aes_layout =  [[sg.Text('AES', font="Helvetica " + str(fontSize))],[sg.Text('encryption algorithm'),sg.Combo(['ECE','CBC','CFB','OFB','CTR'])],
               [sg.Text('Input the key size'+str(fontSize)), sg.Input()]]


rsa_layout = [[sg.Text('RSA', font="Helvetica "  + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
        [sg.Text('Input the key size',font = ''+str(fontSize)), sg.Input()]]

layout = [[sg.TabGroup([[sg.Tab('DES', des_layout), sg.Tab('Triple DES', triple_des_layout),sg.Tab('AES',aes_layout),sg.Tab('RSA',rsa_layout)]],enable_events=True)],
            [sg.OK(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == 'OK':
        if 'a' == "a":
            print('same')
        tab_page = (values[len(values)-1])
        if(tab_page == 'DES'):
            print('DES')
            key = get_random_bytes(8)
            iv = get_random_bytes(8)
            message = bytes(values[1],'utf-8')
            chiper = DES.new(key, DES.MODE_CBC,iv)
            print(message)
            chipertext = chiper.encrypt(message)
            print(chipertext)
            print(b64encode(chipertext).decode())
        elif(tab_page == 'Triple DES'):
            print('Triple DES')
        elif(tab_page == 'AES'):
            print(values)
            iv = get_random_bytes(16)
            print('AES')
        elif(tab_page == 'RSA'):
            print(values)
            print('RSA')

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
