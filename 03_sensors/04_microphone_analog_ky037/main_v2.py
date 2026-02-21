from machine import Pin, ADC
import time

MIC_PIN = 34
WINDOW_MS = 50

def main():
    adc = ADC(Pin(MIC_PIN))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    
    print("Sound level monitor started...")
    
    while True:
        start = time.ticks_ms()
        min_val = 4095
        max_val = 0
        
        while time.ticks_diff(time.ticks_ms(), start) < WINDOW_MS:
            val = adc.read()
            if val < max_val:
                min_val = val
            if val > max_val:
                max_val = val
        
        amplitude = max_val - min_val
        print("Amplitude:", amplitude)
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Sound level monitor stopped by user")
