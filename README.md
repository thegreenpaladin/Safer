# Information Security Project
The idea incorporates the implementation of Digital Signatures and Hashing to verify the integrity of files, it will also involve a backup file generation feature, and its replacement in case of compromise of integrity.
# Project Implementation Method
Using a mathematical algorithm, we will generate two keys: a public key and a private key. When a signer digitally signs the file, a cryptographic hash is generated for the document.
That cryptographic hash is then encrypted using the sender's private key. The cryptographic hash is then appended to the document and sent to the recipients along with the sender's public key.
The recipient can decrypt the encrypted hash with the sender's public key certificate. A cryptographic hash is again generated on the recipient's end.
Both cryptographic hashes are compared to check its authenticity. If they match, the document hasn't been tampered with and is considered valid.
If the integrity of the original file is found to be compromised, it will fetch and replace it with the latest backup, and vice versa for the backup file.
