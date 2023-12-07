#Put the RSA numbers you found here

def getPQE():
    fr = open('prime.txt','r')
    p = int(fr.readline())
    q = int(fr.readline())
    e = 65537
    fr.close()
    return p, q, e

def RSA_encrypt(C):
    p, q, e = getPQE()
    N = p*q
    msg_ord = [ord(c) for c in C]
    M = int(''.join(str(i) for i in msg_ord))
    encrypt_m = pow(M,e,N)
    return encrypt_m

def createTest():
    fo = open('test.txt', 'w')
    fo.write(str(RSA_encrypt('abcdABCD')))
    fo.close()

def createPass():
    fo = open('pass.txt', 'w')
    fo.write(str(RSA_encrypt('p455w0rd55h')))
    fo.close()

def main():
    createTest()
    createPass()

main()