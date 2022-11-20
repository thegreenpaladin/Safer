from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
import os
key = rsa.generate_private_key(
    backend=crypto_default_backend(),
    public_exponent=65537,
    key_size=2048
)
private_key = key.private_bytes(
    crypto_serialization.Encoding.PEM,
    crypto_serialization.PrivateFormat.PKCS8,
    crypto_serialization.NoEncryption()
)
public_key = key.public_key().public_bytes(
    crypto_serialization.Encoding.OpenSSH,
    crypto_serialization.PublicFormat.OpenSSH
)
if not os.path.isdir('keys'):
    os.mkdir('keys')
if os.path.isdir('keys') and len(os.listdir('keys'))!=0:
    exit()

with open('keys/privatekey.txt', 'wb') as f:
    f.write(private_key)
    f.close()
with open('keys/publickey.txt', 'wb') as f:
    f.write(public_key)
    f.close()
os.chmod('keys/privatekey.txt', 0o600)