# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import base64

import hashlib
from Crypto import Random
import PySimpleGUI as sg
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad
from passlib.hash import des_crypt
from base64 import b64encode, b64decode
from passlib.crypto import des
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

# from Crypto.Util.Padding import pad
from base64 import b64encode
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
import random
import subprocess
from subprocess import CREATE_NEW_CONSOLE
# import crypt
# from passlib.hash import des_crypt
import random
from os import urandom
import os

import codecs
sg.theme('Dark Blue 3')   # Add a little color to your windows
fontSize = 25

class AESCipher(object):
    def __init__(self, key):
        self.blockSize = AES.block_size
        #sha256 -> key length 256, MD5 -> 128, now - 192
        # self.key = hashlib.md5(key.encode()).digest()
        self.key = hashlib.sha256(key.encode()).digest()

    def _pad(self, plainText):
        paddingBytesNum = self.blockSize - len(plainText) % self.blockSize
        asciiString = chr(paddingBytesNum)
        paddingStr = paddingBytesNum * asciiString
        paddedPlainText = plainText + paddingStr
        return paddedPlainText

    @staticmethod
    def _unpad(plainText):
        lastChar = plainText[len(plainText) - 1]
        removingBytes = ord(lastChar)
        return plainText[:-removingBytes]

    def encrypt(self, plainText, mode):
        print("key:", self.key)
        plainText = self._pad(plainText)
        iv = Random.new().read(self.blockSize) 

        cipher = AESswitcher(self.key, mode, iv)
        encryptedText = cipher.encrypt(plainText.encode())
        return b64encode(iv + encryptedText).decode("utf-8")

    def decrypt(self, encryptedText, mode):
        encryptedText = b64decode(encryptedText)
        iv = encryptedText[:self.blockSize]
        cipher = AESswitcher(self.key, mode, iv)
        plainText = cipher.decrypt(encryptedText[self.blockSize:]).decode("utf-8")
        return self._unpad(plainText)

def AESswitcher(key, mode, iv):
    if (mode == 'ECB'):
        print('i am ECB')
        cipher = AES.new(key, AES.MODE_ECB)
    elif (mode == 'CBC'):
        print('i am CBC')
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif (mode == 'CFB'):
        print('i am CFB')
        cipher = AES.new(key, AES.MODE_CFB, iv)
    elif (mode == 'OFB'):
        print('i am OFB')
        cipher = AES.new(key, AES.MODE_CFB, iv)
    elif (mode == 'CTR'):
        print('i am CTR')
        cipher = AES.new(key, AES.MODE_CTR) 
    return cipher


def generateExample():
    print('generate')
    with open('example.txt','w') as examplefile:
        for i in range(1,1000):
            rnd = urandom(8)
            rnd = b64encode(rnd).decode('utf-8')
            print(len(rnd))
            examplefile.write(rnd+'\n')


des_layout = [[sg.Text('DES', font="Helvetica"+str(fontSize)) ,sg.Combo(['ECB','CBC','CFB','OFB','CTR'])],
              [sg.Text('Input the message to encrypt'), sg.Input(key='des_input')]]

triple_des_layout = [[sg.Text('Triple DES', font="Helvetica " + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
                     [sg.Text('Input the key size'+str(fontSize)), sg.Input()]]

aes_layout =  [[sg.Text('AES', font="Helvetica " + str(fontSize))],[sg.Text('encryption algorithm'),sg.Combo(['ECB','CBC','CFB','OFB','CTR'])],
               [sg.Text('Input the key size'+str(fontSize)), sg.Input()],[sg.Text('Input the message to encrypt'), sg.Input()]]


rsa_layout = [[sg.Text('RSA', font="Helvetica "  + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
        [sg.Text('Input the key size',font = ''+str(fontSize)), sg.Input()]]

layout = [[sg.TabGroup([[sg.Tab('DES', des_layout), sg.Tab('Triple DES', triple_des_layout),sg.Tab('AES',aes_layout),sg.Tab('RSA',rsa_layout)]],enable_events=True,key='Tab')], 
# [sg.Output()],
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
            # with open('example.txt', 'r+') as f:
            # dict = (f.read().splitlines())
            # key = generatebytes
            # salt = random.getrandbits(24)
           
            # plaintext = b'passwor1 and 1 wqsd sds'
            plaintext = values['des_input']
            # cipher = DES.new(key, DES.MODE_ECB)
            # plaintext = bytes(plaintext,'utf-8')
            # msg = cipher.encrypt(pad(plaintesxt,8))
            # hashfile.write(str(b64encode(plaintext).decode('utf8')))
            # hashfile.write(':')
            msg = des_crypt.hash(plaintext)
            # hashfile.write(b64encode(msg).decode('utf8'))
            print(msg)
            hashfile.write(msg)
            # hashfile.write('\n')
                    # print(str(chipertext), file=hashfile)  # Python 3.x

            # import subprocess
            # subprocess.Popen('cmd', creationflags=CREATE_NEW_CONSOLE)     
            # os.system("start cmd && cd D:\hashcat\hashcat-6.2.5 && hashcat -m 1500 -a 3 D:\internet\internetsecurity\hashed.txt") 
            # os.system("")
            # os.system('start cmd && D: %% cd .. ')
            # os.system('gnome-terminal -e')
            # import subprocess    
            # cmd_line = "start cmd && cd D:\hashcat\hashcat-6.2.5 && hashcat -m 1500 -a 3 D:\internet\internetsecurity\hashed.txt"
            command = 'hashcat -m 1500 -a 3 D:\internet\internetsecurity\hashed.txt'
            os.system('start cmd /K "cd D:\hashcat\hashcat-6.2.5 && hashcat -m 1500 -a 3 -w 3 --benchmark-all D:\internet\internetsecurity\hashed.txt" ')
            #//start cmd /K "cd D:\hashcat\hashcat-6.2.5 && hashcat -m 1500 -a 3 -w 3 --benchmark-all D:\internet\internetsecurity\hashed.txt"
        elif(tab_page == 'Triple DES'):
            print('Triple DES')

        elif(tab_page == 'AES'):
            print("AES value: ", values)
            mode = values[4]
            oriAESObject = AESCipher(values[5])
            value = values[6]
            print(mode, oriAESObject, value)

            a = oriAESObject.encrypt(value, mode)
            print('encrypted: ', a)

            #simulating getting the same key
            # evaAESObject = AESCipher('123123')
            evaAESObject = AESCipher(values[5])
            try:
                b = evaAESObject.decrypt(a, mode)
                print("decrypt succeed, the value: ", b)
                
            except:
                print("decrypt failed")

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
