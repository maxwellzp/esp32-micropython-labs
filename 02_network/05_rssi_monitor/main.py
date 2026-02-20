import network
import time

try:
    from wifi_config import SSID, PASSWORD
except ImportError:
    raise RuntimeError("Create wifi_config.py from wifi_config.example")

WIFI_TIMEOUT = 10
CHECK_INTERVAL = 5

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to SSID: {SSID}")
        wlan.connect(SSID, PASSWORD)
        
        start = time.time()
        
        while not wlan.isconnected():
            if time.time() - start > WIFI_TIMEOUT:
                print("Connection timeout")
                return None
            time.sleep(0.5)
    
    print("Connected!")
    ip_address, *_ = wlan.ifconfig()
    print("IP:", ip_address)
    
    return wlan

def rssi_to_percent(rssi):
    min_rssi = -90
    max_rssi = -30
    
    if rssi <= min_rssi:
        return 0
    if rssi >= max_rssi:
        return 100
    
    return int((rssi - min_rssi) * 100 / (max_rssi - min_rssi))

def draw_bar(percent):
    bars = int(percent / 10)
    return "[" + "#" * bars + " " * (10 - bars) + "]"

def monitor_rssi(wlan):
    print("Starting RSSI monitor...")
    
    while True:
        if wlan.isconnected():
            rssi = wlan.status("rssi")
            percent = rssi_to_percent(rssi)
            
            print(f"RSSI: {rssi} dBm | Quality: {percent}%", draw_bar(percent))
        else:
            print("Wi-Fi disconnected!")
        
        time.sleep(CHECK_INTERVAL)

def main():
    # https://en.wikipedia.org/wiki/Received_signal_strength_indicator
    # -30 dBm: Phenomenal, max signal strength.
    # -50 dBm to -60 dBm: Excellent, high-speed connection.
    # -60 dBm to -70 dBm: Good, reliable for streaming/browsing.
    # -70 dBm to -80 dBm: Poor, likely to have slow speeds and buffering.
    # -80 dBm to -90 dBm: Unusable, constant disconnection.
    wlan = connect_wifi()
    if not wlan:
        return
    
    try:
        monitor_rssi(wlan)
    except KeyboardInterrupt:
        print("Monitoring stopped by user")
        

if __name__ == "__main__":
    main()
