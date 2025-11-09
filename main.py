
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
    with open("called secret.txt", "a") as f:
        f.write(encript(input("your masage: ")))


def decript(masage: str):
    e_masage = ""
    for i in masage:
        if 97 <= ord(i) <= 122:
            e_masage += ''.join(chr(122 - ord(i) + 97))
        elif 65 <= ord(i) <= 90:
            e_masage +=  ''.join(chr(90 - ord(i) + 65))
        else:
            e_masage += i
    print(e_masage)

decript("sr nb mznv rh blhhr:sr nb mznv rh blhhr:")

