import network
import time

SECURITY_TYPES = {
    0: "Open",
    1: "WEP",
    2: "WPA-PSK",
    3: "WPA2-PSK",
    4: "WPA/WPA2-PSK"
}

def main():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    print("Scanning for WiFi networks...")
    
    networks = wlan.scan()
    
    print(f"Found {len(networks)} networks\n")
    
    for net in networks:
        ssid, bssid, channel, rssi, security, hidden = net
        
        ssid = ssid.decode('utf-8')
        security_name = SECURITY_TYPES.get(security, "Unknown")
        
        print(f"SSID: {ssid}")
        print(f"Channel: {channel}")
        print(f"RSSI: {rssi} dBm")
        print(f"Security: {security_name}")
        print(f"Is hidden? {hidden}")
        print("-" * 40)
        

if __name__ == "__main__":
    main()

