
alphabet = '0123456789qwertyuiopasdfghjklzxcvbnm'

length = 0
state = 0
password = ''
count = 0

while count <= len(alphabet):
    for i in alphabet:
        password = i
        print(password)
        count += 1
        if count == 36:
            count = 0
            generator()
#
# while len(password) < 4:
#     for i in alphabet:
#         password += i
#         print(password)
#         password = ''
# #
# for i in alphabet:
#     for j in alphabet:
#         password = i + j
#         count += 1
#         print(password)
#
# print(count)
