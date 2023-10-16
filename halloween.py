import RPi.GPIO as GPIO
import time

# Define GPIO pins
PIR_PIN = 14  # PIR motion sensor pin
RED_PIN = 21   # Red LED pin
GREEN_PIN = 20  # Green LED pin
BLUE_PIN = 16  # Blue LED pin

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Function to gradually change the RGB color
def fade_color():
    delay_time = 0.01  # Delay time for color fading
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

try:
    while True:
        if GPIO.input(PIR_PIN):  # If motion is detected
            print("Motion detected! Changing RGB color.")
            set_color(255, 0, 0)
            time.sleep(10)
            fade_color()
            time.sleep(2)
            set_color(255, 255, 255)
            time.sleep(10)
        else:
            # print("No motion. LEDs remain off.")
            set_color(0, 0, 0)

except KeyboardInterrupt:
    pass

# Clean up GPIO on exit
GPIO.cleanup()
