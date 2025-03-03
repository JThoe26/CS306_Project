import socket

def udp_client(server_ip, server_port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            message = input("Enter a message to send (type 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            
            # Send the message to the UDP server
            sock.sendto(message.encode(), (server_ip, server_port))
            
            # Optionally, receive a response from the server
            response, _ = sock.recvfrom(4096)
            print("Received response from server:", response.decode())

    finally:
        sock.close()

if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"  # Replace with the server's IP address
    SERVER_PORT = 12345       # Replace with the server's port number
    udp_client(SERVER_IP, SERVER_PORT)