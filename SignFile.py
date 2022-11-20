from ecdsa import SigningKey
from Edit_File_GUI import EditDocument
sk = SigningKey.generate() # uses NIST192p
vk = sk.verifying_key
signature = sk.sign(b"message")
with open('signature/signature.txt', 'wb') as f:
    f.write(signature)
    f.close()
try:
    vk.verify(signature, b"message")
    print("It verifies!")
    editDoc = EditDocument('This is a test')
except:
    print("The signature is not valid.")
    exit()