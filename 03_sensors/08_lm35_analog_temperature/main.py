from machine import Pin, ADC
import time

LM35_PIN = 35
READ_INTERVAL_SEC = 5

def main():
    adc = ADC(Pin(LM35_PIN))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    
    print("LM35 temperature sensor started.")
    
    while True:
        raw = adc.read()
        
        # Convert raw to voltage
        voltage = raw / 4095 * 3.3
        
        # 1°C = 0.01 В
        # °C = volatage × 100
        temperature = voltage * 100
        
        print(f"Raw: {raw}")
        print("Voltage: {:.3}".format(voltage))
        print("Temperature: {:.2f} °C".format(temperature))
        print("*" * 30)
        
        time.sleep(READ_INTERVAL_SEC)
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user")

