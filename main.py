# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import hashlib
from Crypto import Random
import PySimpleGUI as sg
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad
from passlib.hash import des_crypt
from base64 import b64encode, b64decode
from passlib.crypto import des
import random

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


def generateDesKey():
    print('in function')


des_layout = [[sg.Text('DES', font="Helvetica"+str(fontSize)) ,sg.Combo(['ECE','CBC','CFB','OFB','CTR'])],
              [sg.Text('Key size is fixed at 56 bytes'),sg.Input(disabled=True,key = 'des_key'),sg.Button(button_text="Generate Key",key='genDesKey')],
              [sg.Text('Input the message to encrypt'), sg.Input()]
              ]

triple_des_layout = [[sg.Text('Triple DES', font="Helvetica " + str(fontSize)) ,sg.Combo(['Select1', 'Select2'])],
                     [sg.Text('Input the key size'+str(fontSize)), sg.Input()]]

aes_layout =  [[sg.Text('AES', font="Helvetica " + str(fontSize))],[sg.Text('encryption algorithm'),sg.Combo(['ECB','CBC','CFB','OFB','CTR'])],
               [sg.Text('Input the key size'+str(fontSize)), sg.Input()],[sg.Text('Input the message to encrypt'), sg.Input()]]


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
