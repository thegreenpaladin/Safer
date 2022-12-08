from ecdsa import SigningKey, VerifyingKey, BadSignatureError
from Edit_File_GUI import EditDocument
import shutil

message = ''

def readFile(fileName):
    data = ''
    if fileName == 'signature/signature.txt':
        with open(fileName, 'rb') as f:
            data = f.read()
            f.close()
    else:
        with open(fileName, 'r') as f:
            data = f.read()
            f.close()
    return data

def writeFile(fileName, data):
    with open(fileName, 'wb') as f:
        f.write(data)
        f.close()

def isFileEmpty():
    if message == '' and signature == b'':
        return True
    else:
        return False

message = readFile('message.txt')
signature = readFile('signature/signature.txt')

print('File Verification Program\n')

if isFileEmpty():
    sk = SigningKey.generate() # uses NIST192p
    vk = sk.verifying_key
    with open("private.pem", "wb") as f:
        f.write(sk.to_pem())
    with open("public.pem", "wb") as f:
        f.write(vk.to_pem())
    print('The file is empty. Please enter some text to save and sign the file.')
    editDoc = EditDocument(message)
    message = readFile('message.txt')
    signature = sk.sign(message.encode('utf-8'))
    print('Signature: ', signature)
    with open('signature/signature.txt','wb') as f:
        f.write(signature)
    shutil.copy2('message.txt', 'backup/msg_backup.txt')
    print('The file has been signed and saved.')
else:
    sk='hehe'
    vk='huhu'
    with open("private.pem") as f:
        sk = SigningKey.from_pem(f.read())
    vk = VerifyingKey.from_pem(open("public.pem").read())
    try:
        vk.verify(signature, message.encode('utf-8'))
        print('Signature is valid')
        ch = input('Do you want to edit the file? (y/n): ')
        if ch == 'y':
            editDoc = EditDocument(message)
            message = readFile('message.txt')
            signature = sk.sign(message.encode('utf-8'))
            writeFile('signature/signature.txt', signature)
            shutil.copy2('message.txt', 'backup/msg_backup.txt')
            print('The file has been signed and saved.')
    except:
        print('Signature is invalid. The file contents were tampered. The backup will replace the current version of the file.')
        shutil.copy2('backup/msg_backup.txt', 'message.txt')