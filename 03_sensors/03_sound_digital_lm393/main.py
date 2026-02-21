from machine import Pin
import time

SOUND_PIN = 15

def main():
    sound = Pin(SOUND_PIN, Pin.IN)
    
    print("Sound sensor started...")
    
    while True:
        if sound.value() == 0:
            print("🔉Sound detected!🔉")
            time.sleep(0.3)
        time.sleep(0.01)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Sound sensor stopped by user")
