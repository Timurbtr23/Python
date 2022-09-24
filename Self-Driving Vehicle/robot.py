# TODO Camera AI
# TODO Start/Mid/End
# TODO Mode
# TODO WiFi connect
# TODO Back/Roof Sonic

import RPi.GPIO as GPIO
import time


class Raspberry:

    def __init__(self):
        self.TRIG = 27
        self.ECHO = 20

        self.forward = 24
        self.back = 23
        self.m_pwm = 25
        self.speed = None

        self.servo = 18
        self.s_pwm = 0

        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)

        # setup UltraSonic
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

        # setup l298n
        GPIO.setup(self.forward, GPIO.OUT)
        GPIO.setup(self.back, GPIO.OUT)
        GPIO.setup(self.m_pwm, GPIO.OUT)

        # setup motors
        GPIO.output(self.forward, GPIO.LOW)
        GPIO.output(self.back, GPIO.LOW)
        self.speed = GPIO.PWM(self.m_pwm, 1000)

        # setup Servo
        GPIO.setup(self.servo, GPIO.OUT)
        self.s_pwm = GPIO.PWM(self.servo, 50)
        self.s_pwm.start(5)

    def mode(self, mode):
        # Need ROS
        if mode == 'self':
            Car().start_move()
        elif mode == 'manual':
            pass


class UltraSonic:

    def __init__(self):
        self.distance = 0

    def scan(self):
        while True:
            pulse_start, pulse_end = 0, 0

            GPIO.output(Car.TRIG, False)
            print("Waiting For Sensor To Settle")

            GPIO.output(Raspberry.TRIG, True)
            time.sleep(0.00001)
            GPIO.output(Raspberry.TRIG, False)

            while GPIO.input(Raspberry.ECHO) == 0:
                pulse_start = time.time()
            while GPIO.input(Raspberry.ECHO) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            self.distance = pulse_duration * 17150
            self.distance = round(distance, 2)

            print("Distance:", self.distance, "cm")

    def check(self):
        self.scan()
        if self.distance > 20:
            Car.move = "forward"
        else:
            Car.move = "stop"
            Motor().stop()


class Servo:

    def __init__(self):
        self.angle = 0

    def left(self):
        pass

    def right(self):
        pass

    def center(self):
        pass


class Motor:

    def __init__(self):
        self.zero = 0
        self.slow = 25
        self.normal = 50
        self.fast = 75

    def change_speed(self, value):
        Raspberry.speed.start(value)

    def acceleration(self, value):
        pause_time = 0.08
        for i in range(0, value+1):
            self.change_speed(i)
            time.sleep(pause_time)

    def stop(self):
        GPIO.output(Raspberry.forward, GPIO.LOW)
        GPIO.output(Raspberry.back, GPIO.LOW)
        self.change_speed(self.zero)
        Car.move = "stop"
        print("stop")

    def forward(self, slow):
        GPIO.output(Raspberry.forward, GPIO.HIGH)
        GPIO.output(Raspberry.back, GPIO.LOW)
        if slow == 'slow':
            self.change_speed(self.slow)
        else:
            self.change_speed(self.normal)
        Car.move = "forward"
        print("forward")

    def back(self):
        GPIO.output(Raspberry.forward, GPIO.LOW)
        GPIO.output(Raspberry.back, GPIO.HIGH)
        self.change_speed(self.slow)
        Car.move = "back"
        print("back")


class Car:

    def __init__(self):
        self.move = "stop"

    def start_move(self):
        UltraSonic().check()
        if not self.check_overtake():
            Motor().acceleration(Motor.normal)

    def check_overtake(self):
        UltraSonic().check()
        if self.move == "forward":
            return False
        else:
            self.overtake()
            return True

    def overtake(self):
        Motor().back()
        time.sleep(1)
        Motor().stop()
        #  TODO Check near upgrade
        Servo().left()
        Motor().forward("slow")
        time.sleep(0.5)
        Servo().center()
        time.sleep(0.5)
        Servo().right()
        time.sleep(0.5)
        Servo().center()
        time.sleep(2.5)
        Servo().right()
        time.sleep(0.5)
        Servo().center()
        time.sleep(0.5)
        Servo().left()
        time.sleep(0.5)
        Servo().center()

    def direction(self):
        if self.move == "forward":
            Motor().forward('normal')
        elif self.move == "stop":
            Motor().stop()
        elif self.move == "back":
            Motor().back()


try:
    Raspberry = Raspberry()
    UltraSonic = UltraSonic()
    Servo = Servo()
    Motor = Motor()
    Car = Car()

    Car.start_move()
finally:
    Raspberry.m_pwm.stop()
    Raspberry.s_pwm.stop()
    GPIO.cleanup()
