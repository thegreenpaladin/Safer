from ecdsa import SigningKey, VerifyingKey
import shutil

class FileIO:
    def __init__(self):
        pass
     
    def appendToFile(self,fileName,text):
        with open(fileName, 'a') as f:
            f.write(text)
            f.close()
            
    def readFile(self, fileName):
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

    def writeFile(self, fileName, data):
        with open(fileName, 'wb') as f:
            f.write(data)
            f.close()

    def createBackup(self):
        shutil.copy2('data/message.txt', 'backup/msg_backup.txt')
    def replaceWithBackup(self):
        shutil.copy2('backup/msg_backup.txt', 'data/message.txt')

    def writeKey(self, fileName, k):
        with open(fileName, "wb") as f:
            f.write(k.to_pem())
            
    def readSigningKey(self, fileName):
        with open(fileName) as f:
            sk = SigningKey.from_pem(f.read())
        return sk

    def readVerifyingKey(self, fileName):
        vk = VerifyingKey.from_pem(open(fileName).read())
        return vk