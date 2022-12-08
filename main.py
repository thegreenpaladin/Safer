from ecdsa import SigningKey
from HelperClasses.Edit_File_GUI import EditDocument
from HelperClasses.FileIO import FileIO
from tkinter import messagebox
from tkinter.messagebox import askyesno
import time, os
import emoji


FileHandler=FileIO()
message = FileHandler.readFile('data/message.txt')
signature = FileHandler.readFile('signature/signature.txt')

def firstTimeProgramExecution():
        if message == '' and signature == b'':
            return True
        else:
            return False

messagebox.showinfo('IS Project', ' Welcome to File Integrity Verification System and Backup System. \U0001F606\U0001F606\U0001F606')

if firstTimeProgramExecution():
    sk = SigningKey.generate() # uses NIST192p
    vk = sk.verifying_key
    FileHandler.writeKey('keys/private.pem', sk)
    FileHandler.writeKey('keys/public.pem', vk)
    messagebox.showinfo("First Time", "A new file has just been created. Add any text you like.")
    editDoc = EditDocument('')
    message = FileHandler.readFile('data/message.txt')
    signature = sk.sign(message.encode('utf-8'))
    FileHandler.writeFile('signature/signature.txt', signature)
    FileHandler.createBackup()
    messagebox.showinfo('Saved and Backed up','The file has been signed and saved. And a backup has been created.'+emoji.emojize(":winking_face_with_tongue:")+''+emoji.emojize(":winking_face_with_tongue:")+''+emoji.emojize(":winking_face_with_tongue:"))
else:
    sk=FileHandler.readSigningKey('keys/private.pem')
    vk=FileHandler.readVerifyingKey('keys/public.pem')
    try:
        vk.verify(signature, message.encode('utf-8'))
        answer = askyesno(title='Integrity Verified!',
                    message='Signature is valid!\nThis file was last modified on: '+ time.ctime(os.path.getmtime('data/message.txt'))+'\nDo you want to edit the file?')
        if answer:
            editDoc = EditDocument(message)
            message = FileHandler.readFile('data/message.txt')
            signature = sk.sign(message.encode('utf-8'))
            FileHandler.writeFile('signature/signature.txt', signature)
            FileHandler.createBackup()
            messagebox.showinfo('Saved and Backed up','The file has been signed and saved. And a backup has been created.'+emoji.emojize(":winking_face_with_tongue:")+''+emoji.emojize(":winking_face_with_tongue:")+''+emoji.emojize(":winking_face_with_tongue:"))
        else:
            messagebox.showinfo('Program Terminating','Terminating Program.')
    except:
        FileHandler.replaceWithBackup()
        backUpFileModificationTime= time.ctime(os.path.getmtime('backup/msg_backup.txt'))
        messagebox.showinfo('Oops! Invalid Signature','Signature is invalid. The file contents were tampered. The current version of the file has been replaced by backup created on:'+backUpFileModificationTime)
        
