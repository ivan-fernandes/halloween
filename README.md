# Raspberry Pi LED Control Script

This Python script is designed to run on a Raspberry Pi to control an LED in response to motion detection via a PIR sensor or based on specific time intervals. It can also simulate flickering like a candle and control an RGB LED.

## Requirements

To use this script, you'll need the following hardware components connected to your Raspberry Pi:

- PIR motion sensor on GPIO pin 14
- Red LED on GPIO pin 21
- Green LED on GPIO pin 20
- Blue LED on GPIO pin 16
- Laser diode (e.g., 650nm Red) on GPIO pin 4 (extra)

Make sure you have the necessary Python libraries installed, including RPi.GPIO.

## Script Overview

- The script initializes the GPIO pins and functions for LED control.
- It includes a function to gradually change the RGB color.
- There's a function to set the RGB color.
- Another function simulates flickering of the LED in a candle-like manner.
- The `laser` function controls a laser diode.
- The main part of the script continuously monitors the PIR sensor and the time. When motion is detected or during specific time intervals (e.g., evening hours), it activates the LED in different ways.
- If motion is detected, it changes the LED color and simulates flickering.

## Usage

1. Make sure the required hardware is connected to the specified GPIO pins on your Raspberry Pi.
2. Ensure that you have the RPi.GPIO library installed on your Raspberry Pi.
3. Save the script to a file (e.g., `halloween.py`) on your Raspberry Pi.
4. Run the script using the following command:

   ```bash
   python3 halloween.py

## Running the Script on Startup

You can configure your Raspberry Pi to start this script automatically on system boot using `systemd`. This ensures that your LED control script runs in the background whenever your Raspberry Pi starts up.

Here are the steps to set up automatic startup:

1. **Create a systemd service unit file**:

   Open a terminal and create a systemd service unit file, typically ending with a `.service` extension, for your script. Use a text editor to create the file. For example, let's call it `halloween.service`:

   ```bash
   sudo nano /etc/systemd/system/halloween.service

2. **Add the following content to your halloween.service file**
   ```bash
   [Unit]
   Description=Halloween script to control LED

   [Service]
   ExecStart=/usr/bin/python3 /path_to_your_script/halloween.py

   [Install]
   WantedBy=multi-user.target

Make sure you replace the path of the python script in the ExecStart section

3. **Enable the service on start up**
sudo systemctl enable halloween.service

4. **Start or stop the service, whenever necessary**
- sudo systemctl start halloween.service
- sudo systemctl stop halloween.service


5. **TO DOs for improving the performance and learning extra skills**
- Play sound on a buzzer to scare people
- Connect it to Alexa to play a spooky sound
- Use a IR transmitter and receiver
- ...
