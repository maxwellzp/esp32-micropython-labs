from machine import Pin, ADC
import time

MIC_PIN = 34

def main():
    adc = ADC(Pin(MIC_PIN))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    
    print("Microphone analog monitor started...")
    
    while True:
        value = adc.read() #0 - 4095
        print(f"Raw: {value}")
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Microphone analog monitor stopped by user")
