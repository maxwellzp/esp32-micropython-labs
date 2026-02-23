from machine import Pin, ADC
import time

LDR_PIN = 34
READ_INTERVAL_SEC = 0.5

def main():
    adc = ADC(Pin(LDR_PIN))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    
    print("LDR light sensor started...")
    
    while True:
        value = adc.read() #0-4095
        print(f"Raw: {value}")
        time.sleep(READ_INTERVAL_SEC)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user")

# Sensor: GL5516
# LDR — Light Dependent Resistor
# 4095 - light
# 0 - dark
