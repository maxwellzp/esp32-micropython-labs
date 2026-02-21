from machine import Pin
import time

PIR_PIN = 13
WARMUP_TIME_SEC = 30
POLL_INTERVAL_SEC = 0.1

def main():
    pir = Pin(PIR_PIN, Pin.IN)
    
    print("PIR motion sensor started...") # PIR = Passive InfraRed.
    print(f"Warming up({WARMUP_TIME_SEC} seconds)...")
    
    time.sleep(WARMUP_TIME_SEC)
    
    print("Ready!")
    
    motion_state = 0
    
    while True:
        current = pir.value()
        
        if current == 1 and motion_state == 0:
            print("Motion START")
            motion_state = 1
        elif current == 0 and motion_state == 1:
            print("Motion END")
            motion_state = 0

        time.sleep(POLL_INTERVAL_SEC)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("PIR motion sensor stopped by user")

