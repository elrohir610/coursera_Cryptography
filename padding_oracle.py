import urllib2
import sys

def strxor(a, b):     # xor two strings of different lengths
        if len(a) > len(b):
                return "".join([str(hex(int(x,16) ^ int(y,16)))[2:] for (x, y) in zip(a[:len(b)], b)])
        else:
                return "".join([str(hex(int(x,16) ^ int(y,16)))[2:] for (x, y) in zip(a, b[:len(a)])])


def int_2_hexstr(n):
        o = str(hex(n))[2:]
        if (len(o)==1):
                o = '0' + o
        return o

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

#if __name__ == "__main__":
#    po = PaddingOracle()
#    po.query(sys.argv[1])       # Issue HTTP query with the given argument

ciphertext = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'

iv = ciphertext[0:32]
b1 = ciphertext[32:64]
b2 = ciphertext[64:96]
b3 = ciphertext[96:]

po = PaddingOracle()

#guess b1
actual = ''
#for i in range(16):
i= 0

for j in range(256):
	guess = int_2_hexstr(j)
	attemp = guess+actual
	pad_l = len(attemp)/2
	pad = ''
	for k in range(pad_l):
		pad = pad + int_2_hexstr(pad_l)
	target = b1[(30-i*2):]
	target = strxor(target,attemp)
	target = strxor(target,pad)
	q_str = iv + b1[0:(30-i*2)] + target
		
	if(po.query(q_str)):
		print q_str
		print attemp
