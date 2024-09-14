from machine import Pin, I2C
import time
from rfid import RFID  # Placeholder for RFID module
from keypad import Keypad  # Placeholder for Keypad module
from display import Display  # Placeholder for Display module

# Define pins
led_success = Pin(2, Pin.OUT)
led_error = Pin(3, Pin.OUT)
rfid_reader = RFID()  # Initialize RFID reader
keypad = Keypad()  # Initialize Keypad
display = Display()  # Initialize Display

# Define passcodes
valid_passcodes = {
    '1234': 'User1',
    '5678': 'User2'
}

def authenticate_rfid():
    # Function to authenticate RFID
    uid = rfid_reader.read_uid()
    if uid:
        display.show_message("RFID Scanned. Enter Passcode:")
        return True
    else:
        display.show_message("RFID Scan Failed.")
        led_error.on()
        time.sleep(1)
        led_error.off()
        return False

def authenticate_passcode():
    # Function to authenticate passcode
    passcode = keypad.get_passcode()
    if passcode in valid_passcodes:
        display.show_message("Access Granted")
        led_success.on()
        time.sleep(2)
        led_success.off()
        return True
    else:
        display.show_message("Access Denied")
        led_error.on()
        time.sleep(1)
        led_error.off()
        return False

def main():
    while True:
        if authenticate_rfid():
            if authenticate_passcode():
                # Unlock the door
                pass
            else:
                # Optionally add a retry mechanism or log failed attempts
                pass
        time.sleep(5)  # Wait before next authentication attempt

if __name__ == "__main__":
    main()
