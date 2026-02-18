from machine import Pin
import time

LED_PIN = 2
BLINK_DELAY = 1

def main():
    led = Pin(LED_PIN, Pin.OUT)
    try:
        while True:
            led.on()
            time.sleep(BLINK_DELAY)
            led.off()
            time.sleep(BLINK_DELAY)
    except KeyboardInterrupt:
        led.off()
        print("Program stopped by user")

if __name__ == "__main__":
    main()
