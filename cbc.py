'''
    File name: AES_modeECB.py
    Author: Emely da Mata
    Title: TP03
    Python Version: 3.8.5

'''

#Imports
from PIL import BmpImagePlugin
import hashlib
from itertools import cycle
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

#Gerar chave aleatoria

key = os.urandom(32)
key

# initialization vector
iv = os.urandom(16)
iv

#Lendo e manipulando imagem de entrada em formato bmp:

input_image = BmpImagePlugin.BmpImageFile("teste.bmp")

image_data = input_image.tobytes()

# cifrando o dado com algoritmo AES no modo CBC:

# 1 - o objeto que criptografa AES com a chave gerada
aes = algorithms.AES(key)

# 2 - o  modo CBC em inicialização
cbc = modes.CBC(iv)

# 3 - criando e encriptando a partir do cipher
cipher = Cipher(aes, cbc, backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(image_data) + encryptor.finalize()
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize()


#  salvando a imagem com a cifra:
output_image = input_image.copy()
output_image.frombytes(ct)
output_image.save("testecbc.bmp")

