import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import subprocess

def decrypt(data):
    key = get_encryption_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(data.encode())
    return decrypted_data.decode()

def get_encryption_key():
    if os.name == 'nt':
        # data = subprocess.check_output('hostname').decode().split('\n')[0].strip() 
        data = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    else:
        with open("/etc/machine-id", 'rb') as f:
            id = f.readline()
        data = str(id.decode()).replace("\n", "")

    salt = data.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(data.encode()))
    return key


def encrypt(data):
    key = get_encryption_key()
    data_byte = data.encode()
    f = Fernet(key)
    encrypted_data = f.encrypt(data_byte)
    return encrypted_data.decode()
