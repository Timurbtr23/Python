print("Zadej radu zavorek:")
zavorky = input()

for i in zavorky:
    if (i != '(') and (i != ')'):
        print("Chyba!")
        exit()

print(zavorky)
len = len(zavorky)

for i in range(len-1):
    if zavorky[i] == ")":
        if zavorky[i-1] == "(":
            zav

