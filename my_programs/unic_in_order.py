def uio(string):
    a = []
    previous = ""
    for i in string:
        if i not in a or i != previous:
            a.append(i)
        previous = i
    return a


print(uio(""))
