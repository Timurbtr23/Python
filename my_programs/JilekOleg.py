import random
import time


def Jilek():
    arr1, arr2 = [], []
    ans, num = 0, 0

    for i in range(1000):
        arr1.append(random.randint(0, 1000))
    for i in range(1001):
        arr2.append(0)

    for i in arr1:
        arr2[i] += 1

    for i in range(len(arr2) - 1):
        if arr2[i] > ans:
            ans = arr2[i]
            num = i


count = 0
for i in range(100):
    start_time = time.time()
    Jilek()
    count += ((time.time() - start_time) * 100000)

print(count / 100)
