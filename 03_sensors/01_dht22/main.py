import dht
from machine import Pin
import time

DHT_PIN = 4
MEASURE_INTERVAL = 10

sensor = dht.DHT22(Pin(DHT_PIN))


def main():
    while True:
        try:
            sensor.measure()
            
            temperature = sensor.temperature()
            humidity = sensor.humidity()
            
            print(f"Temperature: {temperature:.1f} °C")
            print(f"Humidity: {humidity:.1f} %")
            print("-" * 25)
        except OSError as e:
            print("Sensor error:", e)

        time.sleep(MEASURE_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program stopped by user")

# -------------------------
# Temperature: 23.3 °C
# Humidity: 39.9 %
# -------------------------
# Temperature: 23.2 °C
# Humidity: 39.8 %
# -------------------------
# Temperature: 23.2 °C
# Humidity: 39.7 %
# -------------------------
