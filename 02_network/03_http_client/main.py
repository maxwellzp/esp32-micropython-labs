import network
import time
import urequests

WIFI_TIMEOUT = 10

try:
    from wifi_config import SSID, PASSWORD
except ImportError:
    raise RuntimeError("Create wifi_config.py from wifi_config.example")

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(SSID, PASSWORD)
        
        start = time.time()
        
        while not wlan.isconnected():
            if time.time() - start > WIFI_TIMEOUT:
                print("Connection timeout")
                return None
            time.sleep(0.5)
    print("Connected!")
    return wlan

def send_request(api_url):
    response = None
    try:
        response = urequests.get(api_url)
        
        if response.status_code != 200:
            print("HTTP error:", response.status_code)
            return
        
        data = response.json()
        
        print("Id", data["id"])
        print("userId", data["userId"])
        print("Title:", data["title"])
        print("Completed:", data["completed"])
    
    finally:
        if response:
            response.close()

def main():
    wlan = connect_wifi()
    
    if not wlan:
        return
    
    print("Sending HTTP GET request...")
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        send_request(api_url)
    except Exception as e:
        print("HTTP request failed:", e)

if __name__ == "__main__":
    main()
