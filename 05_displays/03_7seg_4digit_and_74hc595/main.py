from machine import Pin
import time

# --- 74HC595 ---
data = Pin(23, Pin.OUT)
clock = Pin(22, Pin.OUT)
latch = Pin(21, Pin.OUT)

digits = [
    Pin(19, Pin.OUT),
    Pin(18, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(17, Pin.OUT)
]

segment_map = {
    0: 0b00111111,
    1: 0b00000110,
    2: 0b01011011,
    3: 0b01001111,
    4: 0b01100110,
    5: 0b01101101,
    6: 0b01111101,
    7: 0b00000111,
    8: 0b01111111,
    9: 0b01101111
}

def shift_out(byte):
    latch.value(0)
    for i in range(8):
        clock.value(0)
        data.value((byte >> (7 - i)) & 1)
        clock.value(1)
    latch.value(1)

def disable_digits():
    for d in digits:
        d.value(1)

def show_number(num):
    s = f"{num:04d}"

    for i in range(4):
        disable_digits()
        shift_out(segment_map[int(s[i])])
        digits[i].value(0)
        time.sleep_ms(2)



def main():
    print("4-digit via 74HC595 (23cnonz e4 sn74hc595n) started...")
    try:
        while True:
            for n in range(10000):
                for _ in range(40):
                    show_number(n)
    except KeyboardInterrupt:
        disable_digits()
        print("Stopped by user")

if __name__ == "__main__":
    main()

