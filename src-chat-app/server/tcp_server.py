import socket
import threading

# TCP server
class TCPServer:
    def __init__(self, host='127.0.0.1', port=65432):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        print(f'TCP Server listening on {host}:{port}')

    def handle_client(self, client_socket, address):
        print(f'Connection from {address} has been established!')
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f'Received from {address}: {message}')
                client_socket.sendall(f'Echo: {message}'.encode('utf-8'))
            except ConnectionResetError:
                break
        client_socket.close()
        print(f'Connection from {address} has been closed.')

    def start(self):
        while True:
            client_socket, address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_thread.start()

if __name__ == '__main__':
    tcp_server = TCPServer()
    tcp_server.start()