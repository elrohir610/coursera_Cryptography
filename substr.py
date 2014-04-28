ciphertext = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'

iv = ciphertext[0:32]
c1 = ciphertext[32:64]
c2 = ciphertext[64:96]
c3 = ciphertext[96:]

print c1
print c1[0:(30-15*2)] + c1[(30-15*2):]
