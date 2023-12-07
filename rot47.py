def rot47(text):
    result = ""
    for char in text:
        if char.isprintable():
            if '!' <= char <= '~':
                result += chr(((ord(char) - 33 + 47) % 94) + 33)
            else:
                result += char
        else:
            result += char
    return result

def main():
    fr = open('prime.txt','r')
    p = fr.readline().rstrip('\n')
    q = fr.readline()
    fr.close()
    fw = open('file7.txt', 'w')
    fw.write(rot47('p = ' + p) + '\n')
    fw.write(rot47('q = ' + q) + '\n')
    fw.write(rot47('e = 65537') + '\n')
    fw.write('It seems this file has been encrypted with rot47')

# file = input("Enter encode file address: ")
main()
