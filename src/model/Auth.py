import flask_login
from src.utilities.json import getJsonDataAsDict, writeDictToJson
import hashlib
import pyaes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

FILEPATH = 'db/pass/pass.json'
users = getJsonDataAsDict(path=FILEPATH)


def AESEncrypt(text, key):
    key = key.ljust(16)[:16].encode()  # The key is adjusted to be 16 bytes
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_text = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_text).decode()

def AESDecrypt(enc_text, key):
    key = key.ljust(16)[:16].encode()  # The key is adjusted to be 16 bytes
    enc_text = base64.b64decode(enc_text)
    iv = enc_text[:16]  # The first 16 bytes are the IV (Initialization Vector)
    encrypted_text = enc_text[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_text), AES.block_size).decode()

class User(flask_login.UserMixin):
    def __init__(self, id):
        self.id = id


class Auther():
    def registerUser(self, uname: str, password: str):
        if uname in users:
            print("Username Already Exists")
            return ValueError
        else:
                
            hashedPass = hashlib.sha256(password.encode()).hexdigest()
            twoTimesHashedPass = hashlib.sha256(hashedPass.encode()).hexdigest()
            
            
            encryptedTTHP = AESEncrypt(twoTimesHashedPass, hashedPass) # encrypted Two Times Hashed Pass
            
            newUser = {
                "password": encryptedTTHP
            }
            
            users[uname] = newUser
            
            writeDictToJson(path=FILEPATH, dictionary=users)
            
            
            
    def checkUser(self, uname: str, password: str):
        if uname in users:
            hashedPass = hashlib.sha256(password.encode()).hexdigest()
            twoTimesHashedPass = hashlib.sha256(hashedPass.encode()).hexdigest()
            
            encrypted = users[uname]["password"]
            try:
                decrypted = AESDecrypt(enc_text=encrypted, key=hashedPass)
            except:
                return False
            
            if decrypted == twoTimesHashedPass:
                return True
            else:
                return False
        else:
            return "Username Not Found"