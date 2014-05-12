import gmpy2
from gmpy2 import mpz
from gmpy2 import invert
from gmpy2 import f_mod
from gmpy2 import powmod
from gmpy2 import isqrt
from gmpy2 import is_prime

N1 = mpz(179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581)

A1 = isqrt(N1)+1
x1 = isqrt(A1*A1-N1)
p1 = A1+x1
q1 = A1-x1
print "========"
print "Q1:"
print p1
print q1
print "========"

N2 = mpz(648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877)

sqrt_N2 = isqrt(N2)
search_interval = 1024*1024

for i in range(search_interval):
	A2 = sqrt_N2+mpz(i+1)
	x2 = isqrt(A2*A2-N2)
	test = (A2+x2)*(A2-x2)
	if test==N2 :
		break

print "========"
print "Q2:"
print A2+x2
print A2-x2
print "========"


N3 = mpz(720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929)

sqrt_N3 = isqrt(mpz(24)*N3) #sqrt(24N)
A3 = sqrt_N3+mpz(1) #2A
diff = A3*A3-mpz(24)*N3 
x3 = isqrt(diff) #2X

p3 = (A3-x3)/6
q3 = (A3+x3)/4 

print "========"
print "Q3:"
print p3
print q3
print "========"

##########################################

c = mpz(22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540)

phi_N1 = mpz(p1-1)*mpz(q1-1)
e = mpz(65537)
d = invert(e,phi_N1)

m = powmod(c,d,N1)
hex_m = ''

while m > 0:
	mod = f_mod(m,16)
	hex_m = str(hex(mod))[2:]+hex_m
	m = (m-mod)/16

hex_m = '0x0'+hex_m
print "========"
print "plain:"
print hex_m
plain_m = '466163746f72696e67206c65747320757320627265616b205253412e'

def hex_2_string(str_i):
        str_o = ""
        i=0
        while i < len(str_i):
                str_o = str_o + chr(int(str_i[i:i+2],16))
                i+=2
        return str_o

print "decode:"
print hex_2_string(plain_m)
