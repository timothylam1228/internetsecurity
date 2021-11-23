# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
# from Crypto.Util.Padding import pad
from base64 import b64encode
from Crypto.Util.Padding import pad, unpad

from passlib.hash import des_crypt
import random
from os import urandom
import os
import codecs
import subprocess

sg.theme('Dark Blue 3')  # Add a little color to your windows
fontSize = 25


def generateDesKey():
    print('in function')


def generateExample():
    print('generate')
    with open('example.txt', 'w') as examplefile:
        for i in range(1, 1000):
            rnd = urandom(8)
            rnd = b64encode(rnd).decode('utf-8')
            print(len(rnd))
            examplefile.write(rnd + '\n')


des_layout = [[sg.Text('DES', font="Helvetica" + str(fontSize)), sg.Combo(['ECE', 'CBC', 'CFB', 'OFB', 'CTR'])],
              #   [sg.Text('Key size is fixed at 56 bytes'),sg.Input(disabled=True,key = 'des_key'),sg.Button(button_text="Generate Key",key='genDesKey')],
              [sg.Text('Input the message to encrypt'), sg.Input(key='des_plaintext')],

              ]

triple_des_layout = [[sg.Text('Triple DES', font="Helvetica " + str(fontSize)), sg.Combo(['Select1', 'Select2'])],
                     [sg.Text('Input the key size' + str(fontSize)), sg.Input()]]

aes_layout = [[sg.Text('AES', font="Helvetica " + str(fontSize))],
              [sg.Text('encryption algorithm'), sg.Combo(['ECE', 'CBC', 'CFB', 'OFB', 'CTR'])],
              [sg.Text('Input the key size' + str(fontSize)), sg.Input()]]

rsa_layout = [[sg.Text('RSA', font="Helvetica " + str(fontSize)), sg.Combo(['Select1', 'Select2'])],
              [sg.Text('Input the key size', font='' + str(fontSize)), sg.Input()]]

layout = [[sg.TabGroup([[sg.Tab('DES', des_layout), sg.Tab('Triple DES', triple_des_layout), sg.Tab('AES', aes_layout),
                         sg.Tab('RSA', rsa_layout)]], enable_events=True, key='Tab')], [sg.Output(size=(60, 15))],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

while True:
    hashfile = open('hashed.txt', 'w')
    event, values = window.read()
    if event == 'genDesKey':
        generatebytes = get_random_bytes(8)
        window['des_key'].update(str(b64encode(generatebytes).decode('utf8')))
    if event == 'OK':
        tab_page = values['Tab']
        if (tab_page == 'DES'):
            # with open('example.txt', 'r+') as f:
            #    dict = (f.read().splitlines())
            #    key = generatebytes
            #    salt = random.getrandbits(24)
            #    print('dict',dict)
            # for plaintext in dict:
            plaintext = values['des_plaintext']
            d = des_crypt.hash(plaintext)
            # cipher = DES.new(key, DES.MODE_ECB)
            plaintext_bytes = bytes(plaintext, 'utf8')
            # msg = cipher.encrypt(plaintext_bytes)
            # hashfile.write(plaintext)
            # hashfile.write(':')
            hashfile.write(d)
            # hashfile.write(msg.decode('ANSI','strict'))
            # print(msg.decode('ANSI','strict'))
            hashfile.write('\n')
            hashfile.close()
            os.system(
                'cd D:\hashcat-6.2.5\hashcat-6.2.5 && hashcat -m 1500 -a 3 D:\internet\internetsecurity\hashed.txt')

            # print(str(chipertext), file=hashfile)  # Python 3.x
            print('done')

        elif (tab_page == 'Triple DES'):
            print('Triple DES')
        elif (tab_page == 'AES'):
            print(values)
            iv = get_random_bytes(16)
            print('AES')
        elif (tab_page == 'RSA'):
            print(values)
            print('RSA')

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
