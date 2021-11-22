# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from passlib.hash import des_crypt
from base64 import b64encode
from passlib.crypto import des
import random

import codecs
sg.theme('Dark Blue 3')   # Add a little color to your windows
fontSize = 25

def generateDesKey():
    print('in function')


des_layout = [[sg.Text('DES', font="Helvetica"+str(fontSize)) ,sg.Combo(['ECE','CBC','CFB','OFB','CTR'])],
              [sg.Text('Key size is fixed at 56 bytes'),sg.Input(disabled=True,key = 'des_key'),sg.Button(button_text="Generate Key",key='genDesKey')],
              [sg.Text('Input the message to encrypt'), sg.Input()]
              ]

triple_des_layout = [[sg.Text('Triple DES', font="Helvetica " + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
                     [sg.Text('Input the key size'+str(fontSize)), sg.Input()]]

aes_layout =  [[sg.Text('AES', font="Helvetica " + str(fontSize))],[sg.Text('encryption algorithm'),sg.Combo(['ECE','CBC','CFB','OFB','CTR'])],
               [sg.Text('Input the key size'+str(fontSize)), sg.Input()]]


rsa_layout = [[sg.Text('RSA', font="Helvetica "  + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
        [sg.Text('Input the key size',font = ''+str(fontSize)), sg.Input()]]

layout = [[sg.TabGroup([[sg.Tab('DES', des_layout), sg.Tab('Triple DES', triple_des_layout),sg.Tab('AES',aes_layout),sg.Tab('RSA',rsa_layout)]],enable_events=True,key='Tab')],
            [sg.OK(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == 'genDesKey':
        generatebytes = get_random_bytes(8)
        window['des_key'].update(str(generatebytes))
    if event == 'OK':
        hashfile = open('example.hash', 'w').close()
        hashfile = open('example.hash', 'a')
        tab_page = values['Tab']
        if(tab_page == 'DES'):
            with open('example.dict', 'r+') as f:
                dict = (f.read().splitlines())
                key = generatebytes
                salt = random.getrandbits(24)
                for plaintext in dict:
                    bytesplaintext = bytes(plaintext,'utf-8')
                    bytesplaintext = pad(bytesplaintext, 8,style='pkcs7')
                    # chiper = DES.new(key, DES.MODE_ECB)
                    # chipertext = chiper.encrypt(bytesplaintext)
                    # chipertext = b64encode(chipertext).decode()
                    print(bytesplaintext)
                    chipertext = des.des_encrypt_block(key,bytesplaintext,salt)
                    print(chipertext)
                    hashfile.write(str(chipertext))
                    hashfile.write('\n')
                    # print(str(chipertext), file=hashfile)  # Python 3.x

            print('done')

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
