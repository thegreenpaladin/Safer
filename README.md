# Information Security Project
The idea incorporates the implementation of Digital Signatures and Hashing to verify the integrity of files, it will also involve a backup file generation feature, and its replacement in case of a compromise of integrity.
# Project Implementation Method
## 1)Digital Signatures
Using a mathematical algorithm, we will generate two keys: a public key and a private key. When a signer digitally signs the file, a cryptographic hash is generated for the document.
## 2)Hashing
That cryptographic hash is then encrypted using the sender's private key. The cryptographic hash can then be used to verify the integrity of the file using the sender's public key and see if it was tampered with.
## 3)Decryption
The recipient can decrypt the encrypted hash with the sender's public key certificate. A cryptographic hash is again generated on the recipient's end.
## 4)Verification
Both cryptographic hashes are compared to check its authenticity. If they match, the document hasn't been tampered with and is considered valid.
## 5)Backup
If the integrity of the original file is found to be compromised, it will fetch and replace it with the latest backup, and vice versa for the backup file.
