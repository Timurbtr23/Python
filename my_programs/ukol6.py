import time
start_time = time.time()

i, j, x, p = 0, 0, 0, 0
c = int(input())

for i in range(c+1):
    j = -1
    while j < i:
        if i == 1:
            p = 3
            x = i * p
        elif i == 2:
            x = i * (3 + (i+1))
        elif i > 2:
            x = i * (3 + p + (i+1))
            p += i+1
        j += i+1

count = ((time.time() - start_time) * 1000)
print(x)
print(count)
