from machine import Pin, PWM
from time import sleep, time

# Define the servo control pin
servo_pin = 26
servo = PWM(Pin(servo_pin), freq=50)  # Initialize PWM

# Define the push button pin
button_pin = 25
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

# Function to set the servo angle
def set_servo_angle(angle):
    min_duty = 40  # Minimum duty cycle (0 degrees)
    max_duty = 105  # Adjusted maximum duty cycle (80 degrees)
    duty = min_duty + (angle / 80) * (max_duty - min_duty)
    servo.duty(int(duty))
    sleep(0.5)  # Allow time for servo to move

# Function to open and close once a day
last_open_time = 0
def daily_open():
    global last_open_time
    current_time = time()
    if current_time - last_open_time >= 86400:  # 86400 seconds in a day
        last_open_time = current_time
        set_servo_angle(30)  # Open position
        sleep(3)
        set_servo_angle(0)  # Closed position

# Main loop
while True:
    daily_open()
    if button.value() == 0:  # Button is pressed
        set_servo_angle(30)  # Open position
        while button.value() == 0:  # Wait while button is held
            sleep(0.1)
        set_servo_angle(0)  # Closed position
    sleep(1)
