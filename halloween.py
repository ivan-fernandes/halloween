import RPi.GPIO as GPIO
import time
from datetime import datetime
import random

# Define GPIO pins
PIR_PIN = 14  # PIR motion sensor pin
RED_PIN = 21   # Red LED pin
GREEN_PIN = 20  # Green LED pin
BLUE_PIN = 16  # Blue LED pin
LASER_PIN = 4 # laser diode 650nm Red

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(LASER_PIN, GPIO.OUT)

# Function to gradually change the RGB color
def fade_color():
    delay_time = 0.02  # Delay time for color fading
    red_value = 255
    green_value = 0
    blue_value = 0

    for _ in range(255):
        red_value -= 1
        green_value += 1
        set_color(red_value, green_value, blue_value)
        time.sleep(delay_time)

    for _ in range(255):
        green_value -= 1
        blue_value += 1
        set_color(red_value, green_value, blue_value)
        time.sleep(delay_time)

    for _ in range(255):
        blue_value -= 1
        red_value += 1
        set_color(red_value, green_value, blue_value)
        time.sleep(delay_time)

# Function to set the RGB color
def set_color(red, green, blue):
    GPIO.output(RED_PIN, red)
    GPIO.output(GREEN_PIN, green)
    GPIO.output(BLUE_PIN, blue)
    
# Function to flicker the LED in a candle-like manner
def flickering(duration_sec):
    start_time = time.time()
    end_time = start_time + duration_sec
    try:
        while time.time() < end_time:
            # Randomly determine whether to turn off the LED
            flicker = random.choice([True, False])
            
            if flicker:
                set_color(0, 0, 0)  # Turn off the LED
            else:
                # Simulate a warm red color
                red_value = random.randint(150, 255)
                #green_value = random.randint(0, 50)
                #blue_value = random.randint(0, 50)
                #set_color(red_value, green_value, blue_value)
                set_color(red_value, 0,0)

            time.sleep(random.uniform(0.1, 0.3))  # Vary the duration of flicker

    except KeyboardInterrupt:
        GPIO.cleanup()

def laser():
   GPIO.output(LASER_PIN, GPIO.HIGH)
   time.sleep(10)
   GPIO.output(LASER_PIN,GPIO.LOW)
   time.sleep(1)
    
try:
    while True:
        h = datetime.now()
        if GPIO.input(PIR_PIN) or ((h.hour> 17 and h.hour <2) and (h.minute in [0,30]) and (h.second>0 and h.second<30)):  # If motion is detected
            # print("Motion detected! Changing RGB color.")
            set_color(255, 0, 0)
            time.sleep(5)
            flickering(25)
            #fade_color()
            #time.sleep(2)
            #set_color(255, 255, 255)
            # laser()
            time.sleep(5)
        else:
            # print("No motion. LEDs remain off.")
            set_color(0, 0, 0)

except KeyboardInterrupt:
    pass

# Clean up GPIO on exit
GPIO.cleanup()
