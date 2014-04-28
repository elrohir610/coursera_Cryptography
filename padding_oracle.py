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

def hex_2_string(str_i):
        str_o = ""
        i=0
        while i < len(str_i):
                str_o = str_o + chr(int(str_i[i:i+2],16))
                i+=2
        return str_o

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
            #print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

#if __name__ == "__main__":
#    po = PaddingOracle()
#    po.query(sys.argv[1])       # Issue HTTP query with the given argument

ciphertext = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'

iv = ciphertext[0:32]
c1 = ciphertext[32:64]
c2 = ciphertext[64:96]
c3 = ciphertext[96:]

po = PaddingOracle()

#guess m1
m1 = ''
for i in range(16):
        print "Round: " + str(i)
        print "Current m1: " + m1
        for j in range(256):
                guess = int_2_hexstr(j)
                attemp = guess+m1
                pad_l = len(attemp)/2
                pad = ''
                for k in range(pad_l):
                        pad = pad + int_2_hexstr(pad_l)
                target = strxor(iv[(30-i*2):],attemp)
                q_str = iv[0:(30-i*2)] + strxor(target,pad) + c1

                if(po.query(q_str)):
                        m1 = attemp
                        break

print "Fina m1: "+m1


#guess m2
m2 = ''
for i in range(16):
	print "Round: " + i
	print "Current m2: " + m2
	for j in range(256):
		guess = int_2_hexstr(j)
		attemp = guess+m2
		pad_l = len(attemp)/2
		pad = ''
		for k in range(pad_l):
			pad = pad + int_2_hexstr(pad_l)
		target = strxor(c1[(30-i*2):],attemp)
		q_str = iv + c1[0:(30-i*2)] + strxor(target,pad) + c2
	
		if(po.query(q_str)):
			m2 = attemp
			break

print "Fina m2: "+m2

#guess m3
m3 = '090909090909090909'
for i in range(9,16,1):
        print "Round: " + str(i)
        print "Current m3: " + m3
        for j in range(256):
                guess = int_2_hexstr(j)
                attemp = guess+m3
                pad_l = len(attemp)/2
                pad = ''
                for k in range(pad_l):
                        pad = pad + int_2_hexstr(pad_l)
                target = strxor(c2[(30-i*2):],attemp)
                q_str = iv+ c1 + c2[0:(30-i*2)] + strxor(target,pad) + c3

                if(po.query(q_str)):
                        m3 = attemp
                        break

print "Fina m3: "+m3

m = m1+m2+m3

print hex_2_string(m)
