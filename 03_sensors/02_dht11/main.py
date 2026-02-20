import dht
from machine import Pin
import time

DHT_PIN = 4
MEASURE_INTERVAL = 10

sensor = dht.DHT11(Pin(DHT_PIN))


def main():
    while True:
        try:
            sensor.measure()
            
            temperature = sensor.temperature()
            humidity = sensor.humidity()
            
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity} %")
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
# Temperature: 24 °C
# Humidity: 26 %
# -------------------------
# Temperature: 24 °C
# Humidity: 26 %
# -------------------------
# Temperature: 24 °C
# Humidity: 26 %
# -------------------------

