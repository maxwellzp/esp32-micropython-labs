from machine import Pin
import time

segments = {
    'a': Pin(23, Pin.OUT),
    'b': Pin(22, Pin.OUT),
    'c': Pin(21, Pin.OUT),
    'd': Pin(19, Pin.OUT),
    'e': Pin(18, Pin.OUT),
    'f': Pin(5, Pin.OUT),
    'g': Pin(17, Pin.OUT),
    'dp': Pin(16, Pin.OUT)
}

digits = [
    Pin(4, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(15, Pin.OUT),
    Pin(13, Pin.OUT)
]

digit_map = {
    0: "abcdef",
    1: "bc",
    2: "abdeg",
    3: "abcdg",
    4: "bcfg",
    5: "acdfg",
    6: "acdefg",
    7: "abc",
    8: "abcdefg",
    9: "abcdfg"
}

def clear_segments():
    for seg in segments.values():
        seg.value(0)

def disable_digits():
    for d in digits:
        d.value(1)

def show_digit(position, number):
    disable_digits()
    clear_segments()

    for seg in digit_map[number]:
        segments[seg].value(1)

    digits[position].value(0)

def show_number(num):
    s = f"{num:04d}"

    for i in range(4):
        show_digit(i, int(s[i]))
        time.sleep_ms(2)

def main():
    print("4-digit 7-segment direct test started...")
    try:
        while True:
            for n in range(10000):
                for _ in range(40):
                    show_number(n)
    except KeyboardInterrupt:
        clear_segments()
        print("Program stopped by user")

if __name__ == "__main__":
    main()
