import os, random, struct
from Crypto.Cipher import AES

iv_i = "4ca00ff4c898d61e1edbf1800618fb28"
iv = ""
i = 0

while i < len(iv_i):
	iv = iv + chr(int(iv_i[i:i+2],16))
	i+=2

print iv
print iv.encode('hex')
