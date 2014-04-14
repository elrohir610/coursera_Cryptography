import os, random, struct
from Crypto.Cipher import AES
from Crypto.Util import Counter

def hex_2_string(str_i):
	str_o = ""
	i=0
	while i < len(str_i):
		str_o = str_o + chr(int(str_i[i:i+2],16))
		i+=2
	return str_o

ciphertext = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
iv = ciphertext[0:32]
iv= hex_2_string(iv)
key = '36f18357be4dbd77f050515c73fcf9f2'
key = hex_2_string(key)
ciphertext = ciphertext[32:]
ciphertext = hex_2_string(ciphertext)

########## CBC
#mode = AES.MODE_CBC
#decryptor = AES.new(key, mode, IV=iv)

########## CTR
mode = AES.MODE_CTR
ctr_e = Counter.new(128, initial_value=long(iv.encode('hex'), 16))
decryptor = AES.new(key, mode, counter=ctr_e)

plain = decryptor.decrypt(ciphertext)
print plain
