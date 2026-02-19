from machine import Pin, PWM
import time

LED_PIN = 13
PWM_FREQ = 1000
STEP_DELAY = 0.005

def main():
    led = PWM(Pin(LED_PIN))
    led.freq(PWM_FREQ)
    
    try:
        while True:
            for duty in range(0, 1024, 5):
                led.duty(duty)
                time.sleep(STEP_DELAY)
            
            for duty in range(1023, -1, -5):
                led.duty(duty)
                time.sleep(STEP_DELAY)        
    
    except KeyboardInterrupt:
        led.duty(0)
        led.deinit()
        print("Program stopped by user")

if __name__ == "__main__":
    main()
