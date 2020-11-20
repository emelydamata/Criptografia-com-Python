'''
    File name: AES_modeECB.py
    Author: Emely da Mata
    Title: TP03
    Python Version: 3.8.5

'''

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

#Lendo e manipulando imagem de entrada em formato bmp:
input_image = BmpImagePlugin.BmpImageFile("teste.bmp")

image_data = input_image.tobytes()

# cifrando o dado com algoritmo AES no modo ECB:

# 1 - o objeto que criptografa AES com a chave gerada
aes = algorithms.AES(key)

# 2 - o  modo CBC em inicialização
ecb = modes.ECB()

# 3 - criando e encriptando a partir do cipher
cipher = Cipher(aes, ecb, backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(image_data) + encryptor.finalize()

#  salvando a imagem com a cifra:
output_image = input_image.copy()
output_image.frombytes(ct)
output_image.save("testeecb4.bmp")

