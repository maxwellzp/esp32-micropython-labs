from machine import Pin
import time

PIR_PIN = 13
WARMUP_TIME_SEC = 30
DETECTION_HOLD_SEC = 1
POLL_INTERVAL_SEC = 0.1

def main():
    pir = Pin(PIR_PIN, Pin.IN)
    
    print("PIR motion sensor started...") # PIR = Passive InfraRed.
    print(f"Warming up({WARMUP_TIME_SEC} seconds)...")
    
    time.sleep(WARMUP_TIME_SEC)
    
    print("Ready!")
    
    while True:
        if pir.value() == 1:
            print("Motion detected!")
            time.sleep(DETECTION_HOLD_SEC)

        time.sleep(POLL_INTERVAL_SEC)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("PIR motion sensor stopped by user")

