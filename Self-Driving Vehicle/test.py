import time

def acceleration(value):
    pause_time = 0.08
    for i in range(0, value + 1):
        time.sleep(pause_time)
        print(i)


acceleration(50)
