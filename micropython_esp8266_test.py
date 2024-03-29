# Author: gabri
# File: micropython_esp8266_test
# Date: 20/01/2020
# Made with PyCharm


from machine import Pin

def main():
    led = Pin(2, Pin.OUT)
    enabled = False
    while True:
        if enabled:
            led.off()
        else:
            led.on()
        utime.sleep_ms(1000)
        enabled = not enabled


if __name__ == '__main__':
    main()
