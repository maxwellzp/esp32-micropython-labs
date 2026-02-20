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

def handle_client(client):
    request = client.recv(1024)
    
    if not request:
        client.close()
        return
    
    request_str = request.decode("utf-8")
    print("Raw request:")
    print(request_str)
    
    request_line = request_str.split("\r\n")[0]
    print("Request line:", request_line)
    
    parts = request_line.split()
    
    if len(parts) < 2:
        client.close()
        return
    
    method = parts[0]
    path = parts[1]
    
    print(f"Method: {method}")
    print(f"Path: {path}")
    
    # Simple routing
    if path == "/":
        body = "<h1>Home page</h1>"
    elif path == "/hello":
        body = "<h1>Hello page</h1>"
    else:
        body = "<h1>404 Not found</h1>"
    
    response = f"""HTTP/1.1 200 OK
        Content-Type: text/html
        Connection: close

        <html>
            <head><title>ESP32 Server</title></head>
            <body>
                {body}
            </body>
        </html>
        """
    
    client.send(response)
    client.close()


def start_server():
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    server.listen(1)
    
    print("Listening on", addr)
    
    try:
        while True:
            client, addr = server.accept()
            print("Client connected:", addr)
            try:
                handle_client(client)
            except Exception as e:
                print("Client error:", e)
            finally:
                client.close()
    except KeyboardInterrupt:
        print("Server stopped by user")
    finally:
        print("Closing server socket")
        server.close()

def main():
    wlan = connect_wifi()
    if not wlan:
        return
    try:
        start_server()
    except Exception as e:
        print("Server error:", e)

if __name__ == "__main__":
    main()

