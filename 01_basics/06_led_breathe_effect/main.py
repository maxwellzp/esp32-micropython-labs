from machine import Pin, PWM
import time
import math

LED_PIN = 13
PWM_FREQ = 1000
STEP_DELAY = 0.02

def main():
    led = PWM(Pin(LED_PIN))
    led.freq(PWM_FREQ)

    angle = 0

    try:
        while True:
            value = (math.sin(angle) + 1) / 2  # 0 .. 1
            duty = int(value * 1023)           # 0 .. 1023

            led.duty(duty)

            angle += 0.1
            if angle > 2 * math.pi:
                angle = 0

            time.sleep(STEP_DELAY)

    except KeyboardInterrupt:
        led.duty(0)
        led.deinit()
        print("Program stopped by user")

if __name__ == "__main__":
    main()
