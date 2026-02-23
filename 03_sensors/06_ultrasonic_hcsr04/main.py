from machine import Pin, time_pulse_us
import time

TRIG_PIN = 12
ECHO_PIN = 14

MEASURE_INTERVAL_SEC = 1
SOUND_SPEED = 0.0343

def main():
    trig = Pin(TRIG_PIN, Pin.OUT)
    echo = Pin(ECHO_PIN, Pin.IN)
    
    print("Ultrasonic sensor started...")
    
    while True:
        # Reset TRIG
        trig.value(0)
        time.sleep_us(3)
        
        #  Pulse 10 microseconds
        trig.value(1)
        time.sleep_us(10)
        trig.value(0)
        
        # Measuring the duration of ECHO
        try:
            duration = time_pulse_us(echo, 1, 30000)
            distance = (duration * SOUND_SPEED) / 2
            print(f"Distance: {distance:.2f} cm")
        except OSError:
            print("Out of range")
        
        time.sleep(MEASURE_INTERVAL_SEC)
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ultrasonic sensor stopped by user")


# Real distance = 0.5 m
# 
# Distance measured by sensor:
# Distance: 50.10 cm
# Distance: 50.13 cm
# Distance: 49.80 cm
# Distance: 49.79 cm
# Distance: 49.79 cm
# Distance: 50.13 cm
# Distance: 50.11 cm
# Distance: 50.13 cm
# Distance: 49.77 cm
# Distance: 49.77 cm
# Distance: 50.11 cm
# Distance: 50.11 cm



