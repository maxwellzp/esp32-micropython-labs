import network
import time

try:
    from wifi_config import SSID, PASSWORD
except ImportError:
    raise RuntimeError("Create wifi_config.py from wifi_config.example")


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to SSID: {SSID}")
        wlan.connect(SSID, PASSWORD)
        
        timeout = 10
        start = time.time()
        
        while not wlan.isconnected():
            if time.time() - start > timeout:
                print("Connection timeout")
                return None
            time.sleep(0.5)
    
    print("Connected!")
    ip_address, *_ = wlan.ifconfig()
    print("IP:", ip_address)
    
    return wlan

def main():
    wlan = connect_wifi()
    
    if wlan:
        # https://en.wikipedia.org/wiki/Received_signal_strength_indicator
        # -30 dBm: Phenomenal, max signal strength.
        # -50 dBm to -60 dBm: Excellent, high-speed connection.
        # -60 dBm to -70 dBm: Good, reliable for streaming/browsing.
        # -70 dBm to -80 dBm: Poor, likely to have slow speeds and buffering.
        # -80 dBm to -90 dBm: Unusable, constant disconnection. 
        print("RSSI:", wlan.status('rssi'))

if __name__ == "__main__":
    main()
