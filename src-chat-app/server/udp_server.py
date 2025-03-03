import socket

def start_udp_server(host='127.0.0.1', port=12345):
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind((host, port))
    print(f"UDP server listening on {host}:{port}")

    while True:
        message, client_address = udp_server.recvfrom(1024)
        print(f"Received message from {client_address}: {message.decode()}")
        response = f"Message received: {message.decode()}"
        udp_server.sendto(response.encode(), client_address)

if __name__ == "__main__":
    start_udp_server()