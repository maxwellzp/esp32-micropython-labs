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
}

digits = {
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

def clear():
    for seg in segments.values():
        seg.value(0)

def show_digit(num):
    clear()
    for seg in digits[num]:
        segments[seg].value(1)

def main():
    print("7-segment test started...")
    while True:
        for i in range(10):
            show_digit(i)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("7-segment test stopped by user")

