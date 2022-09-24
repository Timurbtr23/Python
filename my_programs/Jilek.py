import random
import time

def Jilek():
    arr = []
    ans, num = 0, 0
    rep = 1

    for i in range(1000):
        arr.append(random.randint(0, 1000))

    arr.sort()

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            rep += 1
        else:
            if rep > ans:
                ans = rep
                num = arr[i]
            rep = 1


count = 0
avr = 0
for i in range(100):
    start_time = time.time()
    Jilek()
    count += ((time.time() - start_time) * 100000)

print(count / 100)
