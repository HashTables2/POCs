# Background
I had a sample of malware which created its own AES 256 key with the proper BLOBHEADER and imported it using CryptImportKey. It then called CryptDecrypt. 

# Findings
I found that, for this specfic malware, it seems to use the first 16 bytes of the encrypted data as an IV. It then also decrypts the "IV". 

# Code 
The code uses ECB to decrypt the first 16 bytes and then also uses the encrypted 16 bytes as an IV for later using CBC. 
