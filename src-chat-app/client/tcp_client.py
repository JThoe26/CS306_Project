import socket

def start_tcp_client(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.connect((server_ip, server_port))
        print("Connected to TCP server.")

        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            tcp_socket.sendall(message.encode())
            response = tcp_socket.recv(1024)
            print("Received from server:", response.decode())

if __name__ == "__main__":
    SERVER_IP = '127.0.0.1'  # Change to the server's IP address
    SERVER_PORT = 65432       # Change to the server's port
    start_tcp_client(SERVER_IP, SERVER_PORT)