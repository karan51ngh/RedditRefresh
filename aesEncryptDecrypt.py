import base64
import hashlib
import os
from Crypto.Cipher import AES
from authentication import PASSWORD

__key__ = hashlib.sha256(PASSWORD.encode()).digest()

def aesEncrypt(raw):
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    raw = base64.b64encode(pad(raw).encode('utf8'))
    iv = os.urandom(BS)
    cipher = AES.new(key= __key__, mode= AES.MODE_CFB,iv= iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def aesDecrypt(enc):
    unpad = lambda s: s[:-ord(s[-1:])]
    BS = 16
    enc = base64.b64decode(enc)
    iv = enc[:BS]
    cipher = AES.new(__key__, AES.MODE_CFB, iv)
    return unpad(base64.b64decode(cipher.decrypt(enc[BS:])).decode('utf8'))
