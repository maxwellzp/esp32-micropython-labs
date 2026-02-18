from machine import Pin, ADC, PWM
import time

LED_PIN = 2
POT_PIN = 34

def main():
    # Configure LED as PWM
    led = PWM(Pin(LED_PIN))
    led.freq(1000) # 1kHz
    
    # Configure potentiometer
    pot = ADC(Pin(POT_PIN))
    pot.atten(ADC.ATTN_11DB)
    pot.width(ADC.WIDTH_10BIT)
    
    try:
        while True:
            pot_value = pot.read() # 0 -> 1023
            
            led.duty(pot_value) # 0–1023 -> 0–1023
            
            print(f"ADC: {pot_value}")
            
            time.sleep(0.05)
    except KeyboardInterrupt:
        led.duty(0)
        led.deinit()
        print("Program stopped by user")

if __name__ == "__main__":
    main()
