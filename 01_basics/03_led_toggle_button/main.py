from machine import Pin
import time

DEBOUNCE_DELAY = 0.2 # 200 ms
LED_PIN = 2
BUTTON_PIN = 4

def main():
    led = Pin(LED_PIN, Pin.OUT)
    button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
    
    led_state = False
    last_button_state = 1
    
    try:
        while True:
            current_state = button.value()
            
            if last_button_state == 1 and current_state == 0:
                led_state = not led_state
                led.value(led_state)
                print(f"LED state: {led_state}")
                time.sleep(DEBOUNCE_DELAY)
            
            last_button_state = current_state
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        led.off()
        print("Program stopped by user")

if __name__ == "__main__":
    main()