from ecdsa import SigningKey
from Edit_File_GUI import EditDocument
import shutil

sk = SigningKey.generate() # uses NIST192p
vk = sk.verifying_key
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
    if message == '' and signature == '':
        return True
    else:
        return False

message = readFile('message.txt')
signature = readFile('signature/signature.txt')
print('Signature: ', signature)

print('File Verification Program\n')

if isFileEmpty():
    print('The file is empty. Please enter some text to save and sign the file.')
    editDoc = EditDocument(message)
    message = readFile('message.txt')
    signature = sk.sign(message.encode('utf-8'))
    print('Signature: ', signature)
    writeFile('signature/signature.txt', signature)
    shutil.copy2('message.txt', 'backup/msg_backup.txt')
    print('The file has been signed and saved.')
else:
    print("now: ", sk.sign(b'asd'))
    print("read: " , signature)
    if vk.verify(signature, b"asd"):
        print('Signature is valid')
        ch = input('Do you want to edit the file? (y/n): ')
        if ch == 'y':
            editDoc = EditDocument(message)
            message = readFile('message.txt')
            signature = sk.sign(message.encode('utf-8'))
            writeFile('signature/signature.txt', signature)
            shutil.copy2('message.txt', 'backup/msg_backup.txt')
            print('The file has been signed and saved.')
    else:
        print('Signature is invalid')
        shutil.copy2('backup/msg_backup.txt', 'message.txt')