# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import base64

import PySimpleGUI as sg
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from base64 import b64encode

# from Crypto.Util.Padding import pad
from base64 import b64encode
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA

import random

import crypt
# from passlib.hash import des_crypt
import random
from os import urandom
import os

import codecs
sg.theme('Dark Blue 3')   # Add a little color to your windows
fontSize = 25

def generateDesKey():
    print('in function')
def generateExample():
    print('generate')
    with open('example.txt','w') as examplefile:
        for i in range(1,1000):
            rnd = urandom(8)
            rnd = b64encode(rnd).decode('utf-8')
            print(len(rnd))
            examplefile.write(rnd+'\n')


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
    hashfile = open('hashed.txt', 'w')
    event, values = window.read()
    if event == 'genDesKey':
        generatebytes = get_random_bytes(8)
        window['des_key'].update(str(b64encode(generatebytes).decode('utf8')))
    if event == 'OK':
        tab_page = values['Tab']
        if(tab_page == 'DES'):
            with open('example.txt', 'r+') as f:
                dict = (f.read().splitlines())
                key = generatebytes
                salt = random.getrandbits(24)
                for plaintext in dict:
                    # plaintext = b'passwor1 and 1 wqsd sds'
                    plaintext = (bytes(plaintext,'utf8'))
                    cipher = DES.new(key, DES.MODE_ECB)
                    # plaintext = bytes(plaintext,'utf-8')
                    msg = cipher.encrypt(pad(plaintext,8))
                    hashfile.write(str(b64encode(plaintext).decode('utf8')))
                    hashfile.write(':')
                    hashfile.write(b64encode(msg).decode('utf8'))
                    hashfile.write('\n')
                    # print(str(chipertext), file=hashfile)  # Python 3.x

            print('done')

        elif(tab_page == 'Triple DES'):
            print('Triple DES')
        elif(tab_page == 'AES'):
            print(values)
            iv = get_random_bytes(16)
            print('AES')
        elif (tab_page == 'RSA'):
            print(values)
            print('RSA')
            random_generator = Random.new().read
            rsa = RSA.generate(2048, random_generator)

            private_key = rsa.exportKey()

            public_key = rsa.publickey().exportKey()

            with open("public.txt", 'wb') as f:
                f.write(public_key)
            with open("private.txt", 'wb') as f:
                f.write(private_key)

            message = "sth"

            with open("public.txt") as f:
                key = f.read()
                pub_key = RSA.importKey(str(key))
                cipher = PKCS1_cipher.new(pub_key)
                rsa_text = base64.b64encode(cipher.encrypt(bytes(message.encode("utf8"))))
                print('encrypted')
                print(rsa_text.decode('utf-8'))

            with open("private.txt") as f:
                key = f.read()
                pri_key = RSA.importKey(key)
                cipher = PKCS1_cipher.new(pri_key)
                back_text = cipher.decrypt(base64.b64decode(rsa_text), 0)
                print('decrypted')
                print(back_text.decode('utf-8'))

    if event in (sg.WIN_CLOSED, 'Cancel'):
            break



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
