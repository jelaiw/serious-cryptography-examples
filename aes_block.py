from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom

# Pick a random 16-byte key using Python's crypto PRNG.
k = urandom(16)
print("k = {}".format(hexa(k)))

# Create AES-128 block cipher to encrypt a single block.
cipher = Cipher(algorithms.AES(k), modes.ECB())
aes_encrypt = cipher.encryptor()

# Set plaintext block p to all-zero string.
p = '\x00'*16
p = p.encode()

# Encrypt plaintext p (to ciphertext c).
c = aes_encrypt.update(p) + aes_encrypt.finalize()
print("enc({}) = {}".format(hexa(p), hexa(c)))

# Decrypt ciphertext c to plaintext p.
aes_decrypt = cipher.decryptor()
p = aes_decrypt.update(c) + aes_decrypt.finalize()
print("dec({}) = {}".format(hexa(c), hexa(p)))