
def encript(masage: str):
    e_masage = ""
    for i in masage:
        if 97 <= ord(i) <= 122:
            e_masage += ''.join(chr(122 - ord(i) + 97))
        elif 65 <= ord(i) <= 90:
            e_masage +=  ''.join(chr(90 - ord(i) + 65))
        else:
            e_masage += i
    return e_masage

def e_input():
    with open("secret.txt", "a") as f:
        f.write(encript(input("your masage: ")))




def decript(masage: str):
    d_masage = ""
    for i in masage:
        if 97 <= ord(i) <= 122:
            d_masage += ''.join(chr(122 - ord(i) + 97))
        elif 65 <= ord(i) <= 90:
            d_masage +=  ''.join(chr(90 - ord(i) + 65))
        else:
            d_masage += i
    print(d_masage)
a = e_input()



decript("aaa")

