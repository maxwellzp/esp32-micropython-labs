from machine import Pin
import time

LED_PIN = 2
BUTTON_PIN = 4

def main():
    led = Pin(LED_PIN, Pin.OUT)
    button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
    try:
        while True:
            if button.value() == 0:
                led.on()
            else:
                led.off()
            time.sleep(0.01)
    except KeyboardInterrupt:
        led.off()
        print("Program stopped by user")

if __name__ == "__main__":
    main()