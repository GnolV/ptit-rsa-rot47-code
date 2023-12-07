#Complete RSA calculations (a^b mod c = pow(a,b,c))
def RSA(cipher):
    N = p*q
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    decrypt_c = pow(cipher,d,N)
    return num_to_char(str(decrypt_c))

#Convert number to character
def num_to_char(text):
    text_lst = [''.join(c) for c in text]
    decrypt_lst = []
    while(len(text_lst)!=0):
        tmp = text_lst.pop(0)
        if tmp == '1':
            tmp += text_lst.pop(0)
            tmp += text_lst.pop(0)
        else:
            tmp += text_lst.pop(0)
        decrypt_lst.append(int(tmp))
        tmp = ''
    clear_text = ''.join(chr(c) for c in decrypt_lst)
    return clear_text

def main():
    fo = open('cipher.txt','r')
    cipher_text = int(fo.read())
    print('-------------------------------------')
    print('Decoded results: ' + RSA(cipher_text))

main()