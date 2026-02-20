import network
import time
import socket

try:
    from wifi_config import SSID, PASSWORD
except ImportError:
    raise RuntimeError("Create wifi_config.py from wifi_config.example")

WIFI_TIMEOUT = 10

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
    print("IP:", wlan.ifconfig()[0])
    return wlan

def start_server():
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    
    server = socket.socket()
    server.bind(addr)
    server.listen(1)
    
    print("Listening on", addr)
    
    while True:
        client, addr = server.accept()
        print("Client connected from", addr)
        
        request = client.recv(1024)
        print("Request:") #b'GET / HTTP/1.1\r\nHost: 192.168.1.62\r\nUser-Agent: curl/8.5.0\r\nAccept: */*\r\n\r\n'
        print(request)
        
        response = """HTTP/1.1 200 OK
        Content-Type: text/html
        Connection: close

        <html>
            <head><title>ESP32 Server</title></head>
            <body>
                <h1>Hello from ESP32!</h1>
            </body>
        </html>
        """
        client.send(response)
        client.close()


def main():
    wlan = connect_wifi()
    if not wlan:
        return
    try:
        start_server()
    except KeyboardInterrupt:
        print("Server stopped by user")

if __name__ == "__main__":
    main()

