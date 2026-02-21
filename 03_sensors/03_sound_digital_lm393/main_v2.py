from machine import Pin
import time

SOUND_PIN = 15

def main():
    sound = Pin(SOUND_PIN, Pin.IN)
    
    clap_count = 0
    last_trigger = 0
    DEBOUNCE_MS = 300
    
    print("Clap counter started...")
    
    while True:
        if sound.value() == 0:
            
            now = time.ticks_ms()
            if time.ticks_diff(now, last_trigger) > DEBOUNCE_MS:
                clap_count += 1
                print(f"Clap: {clap_count}")
                last_trigger = now
        time.sleep(0.01)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Clap counter stopped by user")
